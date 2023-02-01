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
from .add_option import options_with_help
from rich.console import group
from rich.text import Text
from .print_options_help import print_options_help
from .print_info import print_info
from .UndonutLogo import UndonutLogo
from .command_box import command_box
from rich.table import Table


@group()
def text_group(options: options_with_help):
    yield command_box(UndonutLogo(), Text("usage: jellyml undonut [options] \n",), "undonut")
    yield Text("Undo the last jellyml command.\n")
    table = Table(expand=True, padding=(0, 1), show_lines=True)
    table.add_column("aliases", no_wrap=True)
    table.add_row("undonut")
    table.add_row("undo")
    table.add_row("return")
    yield table
    yield print_options_help(options)


def print_undo_help(options: options_with_help):
    def do_it():
        print_info(text_group(options))
    return do_it


if __name__ == "__main__":
    print_undo_help([])()
