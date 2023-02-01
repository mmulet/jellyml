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
from .add_option import options_with_help
from rich.text import Text
from rich.table import Table

@group()
def print_optional_arguments_help(options: options_with_help):
    optional_arguments = [
        options for options in options if options[0][0].startswith("-")]
    if len(optional_arguments) <= 0:
        return
    yield Text("optional arguments:")
    table = Table(expand=True, padding=(0, 1), show_lines=True)
    table.add_column("option", justify="right", no_wrap=True)
    table.add_column("description")
    for option_tuple in optional_arguments:
        name, description = option_tuple
        table.add_row("\n".join(list(name)), description)
    yield table

if __name__ == "main":
    print_optional_arguments_help()