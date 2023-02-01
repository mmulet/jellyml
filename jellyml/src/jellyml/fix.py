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
from .SubParsersType import SubParsersType
from .CommandDispatcher import CommandDispatcher
from .CommandDict import CommandDict
from .delete_last_history_item import parse_delete_last_history_item_args
from .fix_get_history_path import parse_get_history_path
from .add_help_to_parser import add_help_to_parser
from .fix_clear_history import parse_clear_history_args
from .extract_bundle import parse_extract_bundle_args
from .constants import fix_command_name
from typing import Optional


class FixArgs:
    fix_command: Optional[str]


def parse_fix_args(subparsers: SubParsersType, out_command_dict: CommandDict):

    fix_parser = subparsers.add_parser(fix_command_name, add_help=False, help="""
        Fix the git repository if it is in an unexpected state.
        Use `jellyml fix -h` to see more info.
    """)

    add_help_to_parser("fix_help", fix_parser)
    dispatcher = CommandDispatcher(fix_parser, "fix_command", [
        parse_extract_bundle_args,
                                   parse_delete_last_history_item_args,
                                   parse_get_history_path,
                                   parse_clear_history_args])
    out_command_dict[fix_command_name] = dispatcher.dispatch
