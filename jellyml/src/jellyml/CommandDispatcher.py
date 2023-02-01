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
from typing_extensions import  Any
from .SubParsersType import SubParsersType
from argparse import ArgumentParser
from .CommandDict import CommandDict
from typing import Callable, List


ParseCommand = Callable[[SubParsersType, CommandDict], Any]


class CommandDispatcher:
    def __init__(self, parser: ArgumentParser, command_arg_attr_name: str,  commands: List[ParseCommand]) -> None:
        subparsers = parser.add_subparsers(dest=command_arg_attr_name)
        self.command_arg_attr_name = command_arg_attr_name
        self.command_dict: CommandDict = {}
        for command in commands:
            command(subparsers, self.command_dict)

    def dispatch(self, args: Any) -> int:
        command = getattr(args, self.command_arg_attr_name)
        if command is None or command not in self.command_dict:
            return -12043
        return self.command_dict[command](args)
