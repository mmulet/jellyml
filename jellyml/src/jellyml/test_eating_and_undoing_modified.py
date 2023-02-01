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
from os import remove
from .test_TestRepo import TestRepo
from .test_eating_and_undoing_committed import make_state_A, eat_and_undo
from .test_parse_test_args import parse_test_args


def test(live_test: bool):
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

    then modify A, but don't commit
    with file_A modified
    Call this state C

    then eat the snapshot, and check that the repo is in the correct state
    should be ghe same as state A

    then undo eating the snapshot, and check that the repo is in the correct state
    should be the same as state C

    tests eating from and undoing to a dirty repo, should test
    working with  the stash
    """
    test_repo = TestRepo()
    # make test repo
    make_state_A(test_repo)

    expected_snapshot_file_tree = test_repo.get_file_tree()

    # take a snapshot at this point, and save it to tensor.pt
    tensor_path = test_repo.save_snapshot_to_tensor("tensor.pt")

    # modify the repo, with uncommited changes
    test_repo.write_to_file("file_A", "test2")

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
