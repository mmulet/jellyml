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
import sys
from .constants import eat_command_name, git_command_name, undo_command_name, fix_command_name
from rich import print
from .print_info import print_info
from rich.console import group
from .SecretAward import SecretAward
from rich.panel import Panel
from typing import Optional, List

first_key = [
    "             ▓██████████▓▒░               ",
    "  ┌  ┐ ┬ ┌▒││░┌┐█┌█│██▓┌▒▒┐▒││░│ ┌ ┬ /    ",
    "  \\/│ │█│▓├┤█├┤█├█│███\\/│█││█│▒├ │  ┌   ",
    "  │  │█┴▒└█││█││█└█└███│██│▒└┘█└█└▒│  ┘   ",
    "    ▒█▒███████████▓███████████████▓▒▒░    ",
    "    ▀ ▀ ▀▀▀█████  ▄ ▄    ░░░███▒██▓▓▒░░   ",
    "   ▄█████▄ ▀▀▀   █▀ █      ░░▒▓█████ ▄ ░  ",
    "   ▄  ██  ▄█▀█▄▄ █  █         ░ ▀ ▀  █ ░  ",
    " ███  ██  █   ▄█ █  █  █   ▄█  █ ██  █ ░░ ",
    " ▒▀ ▄██ ▄ █▀▀▀▀  █  █  █  ▄█  ██▄▀█  █ ▒▒ ",
    "  ▀██▀ ▄█▄ █▄▄   █  █  █▄█▀  ▄▀██ █  █ ▒▒ ",
    "   ▄ ▄█▓██▄      ▀  ▀ ▄██▀ ▄█▀ ██ █  █ ░  ",
    "  ░██▒████▓██▒░ ▄▄▄▄███▀  ▀▀ ▄ ▀  █  █▄▄▄ ",
    "   ▒██████████▓ ▀▀▀      ░▓██████▄        ",
    "    ░▓█░███████████████████████████▓▒░    ",
    "     ░▒▓█░████████████████▓████▓█▒▒░      ",
    "        ░▒▓░▓██████████████████▓▒░        ",
    "           ░▒░░█░▓██████████▒▓░           ",
    "               ░▒▓██████▓▒░               "]


eat_key = [
    "      ▒██████▓         ",
    "   █▄▄▄█▄█▀███▄▒░      ",
    "  ▓██▀▄█▄█▀██▄█▀░░     ",
    "    ▀██      ▄▀█▓░░    ",
    "              █▄▓▓░░   ",
    "               ██▄▒▒   ",
    "   ▄▄▄████████▀██▄░░   ",
    " ▄████▄███████▀▄█░░    ",
    " █▒░▒█▄█▀█▄██▄▓▒░░     ",
    " █ ░▒▓▓█▀▄█▄▀▓▓▒░      ",
    " █    ░▒▓██▓▒░         ",
]

git_key = [
    "        ▄███▄          ",
    "      ▄▄▀█████▄        ",
    "    ▄████   ████▄      ",
    "  ▄██████▄ ▄▀█████▄    ",
    " █████████ ██   ████   ",
    " ▀████████ ██▄▄▄███▀   ",
    "   ▀█████▀ ▀█████▀     ",
    "     ▀███   ███▀       ",
    "       ▀█████▀         ",
    "         ▀▀▀           ",
]

undo_key = [
    "▄   ▄                ",
    "█   █ ▄ ▄▄           ",
    "█   █ █▀▄▄█▄▄▄       ",
    " ▀▀▀ ▄▀▄▄▄▀█▄▄▄▒░    ",
    "    █▄▄█▀▄▀▀█▄█▄▄░   ",
    "   █▄█▀█      █▄█▄░  ",
    "   ▒█▀█        █▄▀▒  ",
    "   ░▀▄▄▄      ▄▄▀█▒  ",
    "    ░█▄▄▄▄  ▄▄▄▀█░   ",
    "     ░▀▀▄▄█▄▄▀█▀░    ",
    "        ░▀▀▀▀░       ",
]

fix_key = [
    "    ▄▀▄ ▄▀ █      █",
    "  ▄▀▄ ▄▀   █▄▄    ▓",
    "▄▀▄ ▄▀     █▄▄ ▒░ ▒",
    "▄ ▄▀       ██▄█▄▄░▒",
    "▄▀         ▀▀▀▀▀▀▀▀",
    " ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ",
    " █▒█▄█   █   ██▄▀▓ ",
    " █▄▀▀█▄▄▄█▄▄▄▓▀▀▀▒ ",
    " █ ░██▄▄▄▓ ▄▄▒▀█░▒ ",
    " █▄▄▄▓▀▀▀▒▀▀▀▒▀▄▄░ ",
    " █   ▒ ░▀░▀▀░░   ░ ",
]

keys_and_commands = [
    (eat_key, eat_command_name),
    (git_key, git_command_name),
    (undo_key, undo_command_name),
    (fix_key, fix_command_name),
]


def get_expected_args(lines: List[str]) -> List[str]:
    expected_args: List[str] = []
    for lin in lines:
        split_line = [arg for arg in lin.strip().split(" ") if arg != ""]
        expected_args.extend(split_line)
    return expected_args


def args_match_key(actual_args: List[str], expected_args: List[str]) -> bool:
    if len(actual_args) != len(expected_args):
        return False
    for i, arg in enumerate(actual_args):
        if arg != expected_args[i]:
            return False
    return True


def check_args_match_key(actual_args: List[str], list_of_key_lines: List[str]) -> bool:
    expected_args = get_expected_args(list_of_key_lines)
    key_args = actual_args[:len(expected_args)]
    return args_match_key(key_args, expected_args)


@group()
def first_hint():
    yield "You are very close!"
    yield "If you are getting any errors like, 'command not found' or 'unexpected command', here are some hints:"
    yield "1. Make sure everything is escaped (or not escaped) correctly"
    yield "2. If you are spreading things across multiple lines, a lot of shells require that the line continuation character comes at the very end of the line. Not even whitespace is allowed after it."

    yield """\nThat's all I have for now. Good luck!"""


@group()
def second_hint():
    yield "You are half way there! But you are still missing something."

    yield "\nNot much else I can say without giving too much away. Good luck!"


def process_secret_args() -> Optional[List[str]]:
    first_arg = sys.argv[1]
    if first_arg != "▓██████████▓▒░":
        return None
    first_key_args = sys.argv[1:]
    if not check_args_match_key(first_key_args, first_key):
        print_info(first_hint())
        return None
    second_key_args = first_key_args[len(get_expected_args(first_key)):]

    for key, command in keys_and_commands:
        if check_args_match_key(second_key_args, key):

            print(Panel.fit(SecretAward(), title="Congratulations!", border_style="yellow"))
            return [command] + second_key_args[len(get_expected_args(key)):]

    return None


if __name__ == "__main__":
    if process_secret_args() is not None:
        print("Correct!")

    # import sys
    # expected_arg_lines: list[list[str]] = []
    # expected_args: list[str] = []
    # for lin in first_key:
    #     split_line = [arg for arg in lin.strip().split(" ") if arg != ""]
    #     expected_arg_lines.append(split_line)
    #     expected_args.extend(split_line)

    # args = sys.argv[1:]

    # print(args)
    # print(expected_args)
    # if len(args) != len(expected_args):
    #     print("Invalid number of arguments")
    #     exit(1)

    # for i, arg in enumerate(args):
    #     if arg != expected_args[i]:
    #         print(f"Invalid argument {i}")

    #         print("Expected:")
    #         print(expected_args[i])
    #         print("Got:")
    #         print(args[i])

    #         exit(1)

    # print("")
