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
from rich.table import Table
from .print_info import print_info
from .command_box import command_box
from .FixLogo import FixLogo
from .ShellCode import ShellCode

@group()
def text_group():
    yield command_box(FixLogo(), Text("usage: jellyml fix {delete_last_history_item, get_history_path, ...} ...\n"), "fix")
    yield Text("Fix the git repository if it is in an unexpected state.\n")
    table = Table(expand=True, padding=(0, 1), show_lines=True)
    table.add_column("command", justify="right", no_wrap=True)
    table.add_column("description")
    table.add_row(
        "delete-last-history-item", "Delete the last history item from the jellyml history file.")
    table.add_row("get-history-path",  """Get the location of the history file for this repo.
Useful for debugging.""")
    table.add_row("clear-history",  """Delete the history file.""")
    table.add_row("extract-bundle",
                  "Extract the git bundle from a jelly filled model file.")
    yield table
    yield "Use -h for more information on a specific command."
    yield ShellCode("jellyml fix extract-bundle -h")


def print_fix_help():
    print_info(text_group())


if __name__ == "__main__":
    print_fix_help()
