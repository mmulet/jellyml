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
from .CommandDict import CommandDict
from .add_option import options_with_help, add_option
from .add_help_printer import add_help_printer
from .add_help_to_parser import add_help_to_parser
from .print_fix_clear_history import print_fix_clear_history
from .get_jelly_history_path import get_jelly_history_path_from_git_top_level
from os.path import exists, sep
from os import remove, getcwd
from typing_extensions import Protocol
from dataclasses import dataclass
from typing import Optional


class ClearHistoryArgs(Protocol):
    top_level_git_dir: Optional[str]

@dataclass
class ClearHistoryArgs_dataclass(ClearHistoryArgs):
    top_level_git_dir: Optional[str] = None


def parse_clear_history_args(subparsers: SubParsersType, out_command_dict: CommandDict):
    command_name = "clear-history"
    help_name = "fix_clear_history_help"
    options: options_with_help = []

    delete_last_history_item_parser = subparsers.add_parser(command_name,
                                                            add_help=False,
                                                            help="""Delete the history file.""")
    add_help_to_parser(help_name, delete_last_history_item_parser)
    add_option(options, delete_last_history_item_parser, "-c", "--top_level_git_dir",
               help=f"""The top level git_directory of the 
git repo to fill the model with. 
Defaults to the current working directory.
If your .git folder is at user{sep}repo{sep}.git, you can use
user{sep}repo as the top_level_git_dir.""")

    out_command_dict[command_name] = add_help_printer(clear_history)(
        help_name, print_fix_clear_history(options))  # type: ignore


def clear_history(args: ClearHistoryArgs) -> int:
    jelly_history_path = get_jelly_history_path_from_git_top_level(
        getcwd() if args.top_level_git_dir is None else args.top_level_git_dir)
    if exists(jelly_history_path):
        remove(jelly_history_path)
    return 0
