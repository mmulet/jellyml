# pyright: reportPrivateUsage=false
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
from dataclasses import dataclass
from typing_extensions import Protocol
from .get_code_path import get_code_path
from rich.panel import Panel
from .DonutLogo import DonutLogo
from rich.console import group
from rich.text import Text
from rich import print



class AddCodeArgs(Protocol):
    code: str


@dataclass
class AddCodeArgs_dataclass(AddCodeArgs):
    code: str


def parse_add_code_args(subparsers: SubParsersType, out_command_dict: CommandDict):
    command_name = "add-code"
    git_parser = subparsers.add_parser(command_name,)
    git_parser.add_argument("code")
    out_command_dict[command_name] = add_code


# @group()
# def thanks_message():
#     yield "Thanks for purchasing jellyml! Your contribution will really help me keep this project going. I'm really excited to see what you build with it.",
#     # yield "No more nagging text boxes for you, and if you need anything give me a line at [blue underline]support@jellyml.com[/blue underline]",
#     # yield Text("Thanks again,\nMichael Mulet", justify="right")

@group()
def text_group():
    yield """Thanks for sponsoring jellyml! Your contribution will really help me keep this project going. I'm really excited to see what you build with it."""
    yield "No more nagging text boxes for you. If you need anything, send me a message at [blue underline]support@jellyml.com[/blue underline] and include your GitHub username that you used to sponsor JellyML."
    yield Text("Thanks again,\nMichael Mulet", justify="right")
def add_code(args: AddCodeArgs):
    # This isn't really meant to be secure, just a way to keep
    # honest people honest. Plus I want it to be easy for
    # people who don't want to purchase a code, to 
    # still find the code online
    if not args.code.startswith("you-are-awesome"):
        print("Invalid code")
        return 1
    code_path = get_code_path()
    with open(code_path, "w") as f:
        f.write(args.code)
    print(Panel.fit(DonutLogo(text_group()),
                    title="Thanks!!", border_style="blue"))

    return 0


if __name__ == "__main__":
    print(Panel.fit(DonutLogo(text_group()),
                    title="Thanks!!", border_style="blue"))
