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
from .test_FileTree import compare_file_trees, get_file_tree
from os.path import join
from .git import git, GitArgs_dataclass
from .test_parse_test_args import parse_test_args
from subprocess import run


def test(live_test: bool):
    """"
    test using the git command
    """
    test_repo = TestRepo()
    # make test repo
    make_state_A(test_repo, skip_ignore=True)
    expected_snapshot_file_tree_a = test_repo.get_file_tree()
    # take a snapshot at this point, and save it to tensor.pt
    first_snapshot = test_repo.save_snapshot_to_tensor("a")

    test_clone_path = join(test_repo.output_path, "test_clone")

    if live_test:
        run(f"jellyml git {first_snapshot} clone {{}} {test_clone_path}",
            shell=True, check=True, cwd=test_repo.path)
    else:
        if git(GitArgs_dataclass(
            args=[first_snapshot, "clone", "{}", test_clone_path],
        )) != 0:
            raise Exception("Failed to extract the snapshot")

    actual = get_file_tree(root_path=test_clone_path,
                           git_repo_path=test_clone_path)
    compare_file_trees(
        expected_snapshot_file_tree_a, actual=actual, skip_status_check=True)


if __name__ == '__main__':
    test(parse_test_args().live)

    print("passed")
