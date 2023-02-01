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
from .JellyHistoryArgs import JellyHistoryArgs, add_history_args_to_parser
from .SubParsersType import SubParsersType
from .CommandDict import CommandDict
from .get_jelly_history import get_jelly_history
from .pop_jelly_history import pop_jelly_history
from .add_option import options_with_help
from .add_help_printer import add_help_printer
from .add_help_to_parser import add_help_to_parser
from .print_fix_delete_last_history_item import print_fix_delete_last_history_item
from .Run import Run
from typing import Optional
from dataclasses import dataclass

class DeleteLastHistoryItemArgs(JellyHistoryArgs):
    code_dir: Optional[str]

@dataclass
class DeleteLastHistoryItemArgs_dataclass(JellyHistoryArgs):
    code_dir: Optional[str]


def parse_delete_last_history_item_args(subparsers: SubParsersType, out_command_dict: CommandDict):
    command_name = "delete-last-history-item"
    help_name = "fix_delete_last_history_item_help"
    options: options_with_help = []

    delete_last_history_item_parser = subparsers.add_parser(command_name, add_help=False, help="""
        Delete the last history item from jellyml.the history file.
        """)
    add_help_to_parser(help_name, delete_last_history_item_parser)
    add_history_args_to_parser(options, delete_last_history_item_parser)
    out_command_dict[command_name] = add_help_printer(delete_last_history_item)(
        help_name, print_fix_delete_last_history_item(options))  # type: ignore


def delete_last_history_item(run: Run) -> int:
    history = get_jelly_history(run)
    pop_jelly_history(run, jelly_history=history)
    return 0
