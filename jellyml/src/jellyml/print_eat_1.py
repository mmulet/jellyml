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
from rich.console import group
from rich.text import Text
from .ShellCode import ShellCode
from .print_info import print_info


@group()
def text_group():
    yield Text(f"""
Successfully loaded the snapshot.
If you want to go back to your previous state, you can run this command:""")
    yield ShellCode(f"jelly undo")


def print_eat_1():
    print_info(text_group())


if __name__ == "__main__":
    print_eat_1()
