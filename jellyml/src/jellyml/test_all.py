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
from .test_eating_and_undoing_committed import test as t1
from .test_eating_and_undoing_modified import test as t2
from .test_extract_bundle import test as t3
from .test_git_command import test as t4
from .test_modified_and_committed_snapshot import test as t5
from .test_modified_snapshot import test as t6
from .test_modified_and_branched_snapshot import test as t7
from .test_multiple_eat_and_undo import test as t8

tests = [t1, t2, t3, t4, t5, t6, t7, t8]

if __name__ == '__main__':
    live = parse_test_args().live
    for i, test in enumerate(tests):
        print(f"test {i}")
        test(live)
        print(f"passed")

    print("All tests passed")
