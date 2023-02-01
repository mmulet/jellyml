# pyright: reportUnknownMemberType=false
# Project     jellyml
# @author     Michael Mulet
# @link       github.com/mmulet/jellyml
# @license    LGPLv3 - Copyright (c) 2023 Michael Mulet
#
# This file is part of the jellml library.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from .test_TestRepo import TestRepo
from .test_eating_and_undoing_committed import make_state_A
from .eat import eat, EatArgsWithModel_dataclass
from .undo import undo, UndoArgs_dataclass
from .test_FileTree import compare_file_trees
from .test_parse_test_args import parse_test_args
from subprocess import run
from typing import Callable


def get_created_branch(test_repo: TestRepo) -> str:
    branches = test_repo.run_with_output("git branch").split("\n")
    undo_branches = [b for b in branches if b.startswith("jellyml-undo")]
    if len(undo_branches) != 1:
        raise Exception("expected 1 undo branch, got "+str(undo_branches))
    undo_branch = undo_branches[0]
    return undo_branch


def test_modified_snapshot(live_test: bool, after_eating_shapshot: Callable[[TestRepo], None], get_created_branch: Callable[[TestRepo], str] = get_created_branch):
    test_repo = TestRepo()
    # make test repo
    make_state_A(test_repo)
    expected_snapshot_file_tree_a = test_repo.get_file_tree()
    # take a snapshot at this point, and save it to tensor.pt
    first_snapshot = test_repo.save_snapshot_to_tensor("a")

    # modify the state before eating
    test_repo.write_to_file("file_A", "test_2")
    expected_after_undo = test_repo.get_file_tree()

    if live_test:
        run(f"jellyml eat --quiet {first_snapshot}",
            shell=True, check=True, cwd=test_repo.path)
    else:
        if eat(EatArgsWithModel_dataclass(
                model=first_snapshot,
                quiet=True,
                code_dir=test_repo.path,
                no_donut=False)) != 0:
            raise Exception("Failed to eat the snapshot")
    compare_file_trees(
        expected_snapshot_file_tree_a, actual=test_repo.get_file_tree(), skip_status_check=True)

    # modify the state after eating,
    test_repo.write_to_file("file_A", "test_3")
    after_eating_shapshot(test_repo)
    expected_other_branch = test_repo.get_file_tree()

    if live_test:
        run(f"jellyml undo --quiet",
            shell=True, check=True, cwd=test_repo.path)
    else:
        if undo(UndoArgs_dataclass(
                quiet=True,
                code_dir=test_repo.path,
                no_donut=False)) != 0:
            raise Exception("Failed to undo the snapshot")
    compare_file_trees(
        expected_after_undo, actual=test_repo.get_file_tree())
    # stash the current modified state, don't care about it
    test_repo.run("git stash --quiet --include-untracked")
    undo_branch = get_created_branch(test_repo)
    test_repo.run(f"git checkout --quiet {undo_branch}")
    compare_file_trees(
        expected_other_branch, actual=test_repo.get_file_tree(), skip_status_check=True)


def test(live_test: bool):
    """"
    test modified snapshot. 
    This should cause the modifications to be stored
    in a new branch jellyml-undo-{date}-{uuid}
    """
    def no_op(test_repo: TestRepo):
        pass
    test_modified_snapshot(live_test, after_eating_shapshot=no_op)


if __name__ == '__main__':
    test(parse_test_args().live)

    print("passed")
