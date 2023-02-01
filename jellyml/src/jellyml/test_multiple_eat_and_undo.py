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
from .test_FileTree import compare_file_trees, FileTree
from .test_parse_test_args import parse_test_args
from subprocess import run
from typing import List

def test(live_test: bool):
    """"
    test multiple eating and undoing
    """
    test_repo = TestRepo()
    # make test repo
    make_state_A(test_repo)
    expected_snapshot_file_tree_a = test_repo.get_file_tree()
    # take a snapshot at this point, and save it to tensor.pt
    first_path = test_repo.save_snapshot_to_tensor("a")

    tensors = [first_path]
    expect = [expected_snapshot_file_tree_a]
    for i in range(9):
        test_repo.write_to_file("file_A", "test"+str(i))
        expect.append(test_repo.get_file_tree())
        tensors.append(test_repo.save_snapshot_to_tensor("a_"+str(i)))

    undo_expect: List[FileTree] = []
    for i in range(10):
        undo_expect.append(test_repo.get_file_tree())
        if live_test:
            run(f"jellyml eat --quiet {tensors[i]}",
                shell=True, check=True, cwd=test_repo.path)
        else:
            if eat(EatArgsWithModel_dataclass(
                    model=tensors[i],
                    quiet=True,
                    code_dir=test_repo.path,
                    no_donut=False)) != 0:
                raise Exception("Failed to eat the snapshot")
        actual = test_repo.get_file_tree()
        compare_file_trees(
            expect[i], actual=actual, skip_status_check=True)

    for i in reversed(range(10)):
        if live_test:
            run(f"jellyml undo --quiet",
                shell=True, check=True, cwd=test_repo.path)
        else:
            if undo(UndoArgs_dataclass(
                    quiet=True,
                    code_dir=test_repo.path,
                    no_donut=False)) != 0:
                raise Exception("Failed to undo the snapshot")
        actual = test_repo.get_file_tree()
        compare_file_trees(
            undo_expect[i], actual=actual)


if __name__ == '__main__':
    test(parse_test_args().live)

    print("passed")
