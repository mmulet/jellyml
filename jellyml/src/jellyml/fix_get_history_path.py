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
from .get_jelly_history_path import get_jelly_history_path
from .add_option import options_with_help
from .add_help_printer import add_help_printer
from .print_fix_get_history_path_help import print_fix_get_history_path_help
from .add_help_to_parser import add_help_to_parser
from .Run import Run


class GetHistoryPath(JellyHistoryArgs):
    code_dir: str


def parse_get_history_path(subparsers: SubParsersType, out_command_dict: CommandDict):
    command_name = "get-history-path"
    help_name = "fix_get_history_path_help"
    options: options_with_help = []
    parser = subparsers.add_parser(command_name, add_help=False, help="""
        Get the location of the history file for this repo.
        Useful for debugging.
        """)
    add_help_to_parser(help_name, parser)

    add_history_args_to_parser(options, parser)
    out_command_dict[command_name] = add_help_printer(get_history_path)(
        help_name, print_fix_get_history_path_help(options))  # type: ignore


def get_history_path(args: GetHistoryPath) -> int:
    print(get_jelly_history_path(run=Run(git_repo_path=args.code_dir)))
    return 0
