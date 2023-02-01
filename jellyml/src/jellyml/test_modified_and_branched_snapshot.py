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
from .test_parse_test_args import parse_test_args
from .test_modified_snapshot import test_modified_snapshot
from .test_TestRepo import TestRepo

branch_name = "jellyml-test-after-eat_branch"


def after_eating_shapshot_commit_changes_and_branch(test_repo: TestRepo):
    test_repo.run("git add .")
    test_repo.run(
        "git commit --quiet -m 'commit after eating but before undoing'")
    test_repo.run(f"git checkout --quiet -b {branch_name}")


def get_created_branch(test_repo: TestRepo) -> str:
    branches = test_repo.run_with_output("git branch").split("\n")
    undo_branches = [b for b in branches if b.startswith("jellyml-undo")]
    if len(undo_branches) != 0:
        raise Exception("expected 0 undo branch (should not make one), got "+str(undo_branches))
    found_branch = [b for b in branches if b.startswith(branch_name)]
    if len(found_branch) != 1:
        raise Exception(f"expected to find  {branch_name}")

    return found_branch[0]


def test(live_test: bool):
    """"
    test modified snapshot. 
    This should cause the modifications to be stored
    in a new branch jellyml-undo-{date}-{uuid}
    """
    test_modified_snapshot(
        live_test,
        after_eating_shapshot=after_eating_shapshot_commit_changes_and_branch,
        get_created_branch=get_created_branch)


if __name__ == '__main__':
    test(parse_test_args().live)

    print("passed")
