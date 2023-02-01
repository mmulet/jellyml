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
from .CommandDict import CommandDict
from .SubParsersType import SubParsersType
from .add_option import add_option, options_with_help
from .print_info import print_info
from rich.console import Group, group
from .puzzles import puzzles
from rich.panel import Panel

class PuzzleArgs:
    puzzle_index: int


def parse_puzzle_args(subparsers: SubParsersType, out_command_dict: CommandDict):
    command_name = "puzzle"

    extract_parser = subparsers.add_parser(
        command_name, add_help=True, help="Get the puzzle answer")
    options: options_with_help = []

    add_option(options, extract_parser,  "puzzle_index",
               type=int,
               help="Index of the puzzle to solve")

    out_command_dict[command_name] = puzzle_answer


@group()
def print_puzzle_answer(puzzle_question: str, puzzle_answer: str):
    yield Panel.fit(puzzle_question, title="Puzzle")
    yield Panel.fit(puzzle_answer, title="Answer")
    yield "Thanks for playing!\nIf you have any ideas for new puzzles, open an issue at https://github.com/mmulet/jellyml"


def puzzle_answer(args: PuzzleArgs) -> int:
    if args.puzzle_index < 0 or args.puzzle_index >= len(puzzles):
        print_info(Group(
            f"Puzzle index out of range.\n Must be between 0 and {len(puzzles) -1} inclusive"))
        return 1
    puzzle_question, puzzle_answer = puzzles[args.puzzle_index]
    print_info(print_puzzle_answer(puzzle_question, puzzle_answer))
    return 0
