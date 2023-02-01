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

def after_eating_shapshot_commit_changes(test_repo: TestRepo):
    test_repo.run("git add .")
    test_repo.run(
            "git commit --quiet -m 'commit after eating but before undoing'")

def test(live_test: bool):
    """"
    test modified snapshot. 
    This should cause the modifications to be stored
    in a new branch jellyml-undo-{date}-{uuid}
    """
    test_modified_snapshot(live_test, after_eating_shapshot=after_eating_shapshot_commit_changes)

if __name__ == '__main__':
    test(parse_test_args().live)

    print("passed")
