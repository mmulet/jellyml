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
from typing_extensions import Any
from typing import Callable


def add_help_printer(command: Callable[[Any], int]) -> Callable[[str, Callable[[], None]], Callable[[Any], int]]:
    """
    Example:
    @add_help_printer
    def command(args: Any):
        return do_stuff()

    def_parse_args(subparsers: SubParsersType, out_command_dict: CommandDict):
        command_name = "command"
        def print_help():
            print(f"Usage: jellyml {command_name} [options]")
        out_command_dict[command_name] = command(print_help)

    or

    def command(args: Any):
        return do_stuff()

    def_parse_args(subparsers: SubParsersType, out_command_dict: CommandDict):
        command_name = "command"
        def print_help():
            print(f"Usage: jellyml {command_name} [options]")
        out_command_dict[command_name] = add_help_printer(command)(print_help)

    """
    def wrapper(help_name: str, print_help_function: Callable[[], None]):
        def wrapper2(args: Any):
            if getattr(args, help_name, False):
                print_help_function()
                return 0
            return command(args)
        return wrapper2
    return wrapper
