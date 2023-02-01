#pyright: reportUnknownMemberType=false
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
from .test_FileTree import compare_file_trees, FileTree
from os import remove
from .eat import eat, EatArgsWithModel_dataclass
from .undo import undo, UndoArgs_dataclass
from .test_TestRepo import TestRepo
from subprocess import run
from .test_parse_test_args import parse_test_args


def make_state_A(test_repo: TestRepo, skip_ignore: bool = False):
    # make test repo
    test_repo.write_to_file("file_A", "test")
    test_repo.write_to_file("file_with_unstaged_changes", "commited_test")
    if not skip_ignore:
        test_repo.write_to_file("ignore_me", "ignore this")
    test_repo.write_to_file(".gitignore", "ignore_me")

    test_repo.run('git add -A')
    test_repo.run("git commit --quiet -m 'initial commit'")

    # Make some changes that are unstaged and untracked
    test_repo.write_to_file("untracked_file", "untracked")
    test_repo.write_to_file("file_with_unstaged_changes", "unstaged_change")


def eat_and_undo(live_test: bool,
                 test_repo: TestRepo,
                 tensor_path: str,
                 expected_snapshot_file_tree: FileTree,
                 expected_after_undo_file_tree: FileTree):

    # eat the snapshot, and check that the repo is in the correct state
    # test_repo.run(f"jellyml eat --quiet {tensor_path}")
    if live_test:
        run(f"jellyml eat --quiet {tensor_path}",
            shell=True, check=True, cwd=test_repo.path)
    else:
        if eat(EatArgsWithModel_dataclass(
                model=tensor_path,
                quiet=True,
                code_dir=test_repo.path,
                no_donut=False)) != 0:
            raise Exception("Failed to eat the snapshot")

    # check that the repo is in the correct state
    actual_after_snapshot_file_tree = test_repo.get_file_tree()
    # skip the status check because the snapshot commits everything, so it does not
    # preserve the status of the files
    compare_file_trees(
        expected_snapshot_file_tree, actual_after_snapshot_file_tree, skip_status_check=True)

    # undo eating the snapshot
    # test_repo.run("jellyml undo --quiet")
    if live_test:
        run("jellyml undo --quiet", shell=True, check=True, cwd=test_repo.path)
    else:
        if undo(UndoArgs_dataclass(
                quiet=True,
                code_dir=test_repo.path,
                no_donut=False)) != 0:
            raise Exception("Failed to undo the snapshot")

    # check that the repo is in the correct state
    actual_after_undo_file_tree = test_repo.get_file_tree()
    compare_file_trees(
        expected_after_undo_file_tree, actual_after_undo_file_tree)

    return True


def test(live_test: bool = False):
    """"
    Start with a git repo with the following files:
    Call this state A
      status|file| contents

       clean|file_A  
    modified|file_with_unstaged_changes
     ignored|ignore_me
       clean|.gitignore
   untracked|untracked_file

   create snapshot, save it to tensor.pt

    then make a new commit
    with file_A modified, and untracked_file deleted
    call this state B

    then eat the snapshot, and check that the repo is in the correct state
    should be ghe same as state A

    then undo eating the snapshot, and check that the repo is in the correct state
    should be the same as state B

    tests eating from and undoing to a clean repo
    """
    test_repo = TestRepo()
    # make test repo
    make_state_A(test_repo)
    expected_snapshot_file_tree = test_repo.get_file_tree()

    # take a snapshot at this point, and save it to tensor.pt
    tensor_path = test_repo.save_snapshot_to_tensor("tensor.pt")

    # modify the repo, with a committed change
    test_repo.write_to_file("file_A", "test2")

    test_repo.run('git add file_A')
    test_repo.run("git commit --quiet -m 'second commit'")
    remove(test_repo.join("untracked_file"))
    expected_after_undo_file_tree = test_repo.get_file_tree()

    eat_and_undo(live_test,
                 test_repo,
                 tensor_path,
                 expected_snapshot_file_tree,
                 expected_after_undo_file_tree)


if __name__ == '__main__':
    test(parse_test_args().live)
    print("passed")
