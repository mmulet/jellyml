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
from rich.console import group, Group
from rich.text import Text
from rich.panel import Panel
from rich import print
from .have_purchased_code import have_purchased_code
from os import isatty
from sys import stdout
from .puns import puns
from .puzzles import puzzles
from random import randint
from .ShellCode import ShellCode
from atexit import register


@group()
def purchase_box():
    yield "If you like JellyML, please consider sponsoring it."
    yield Panel.fit(Group("Monthly:\n  [blue underline]https://github.com/sponsors/mmulet", "One-Time:\n  [blue underline]https://github.com/sponsors/mmulet?frequency=one-time[/blue underline]\n\n(some terminals may not follow links)"), title="sponsor now", border_style="yellow", )
    yield Text("""Sponsors will receive a code to disable Puns, Puzzles, and Purchases 
as well as priority for support and feature requests.\n""")
    yield Text("""Also, sponsorships are available for companies 
that want to put their name and logo on the front page
in order to get their product and name in front of
interested AI/ML researchers, engineers, and students.""")
    yield Text("Thank you for your support,\nMichael Mulet\n", justify="right")



@group()
def text_group():
    yield Panel.fit(puns[randint(0, len(puns) - 1)], title="Puns", border_style="blue")
    puzzle_index = randint(0, len(puzzles) - 1)
    puzzle_question, _ = puzzles[puzzle_index]
    yield Panel.fit(Group(
        Text(puzzle_question, justify="center"),
        "\nFor the answer, use this command:",
        ShellCode(f"jellyml puzzle {puzzle_index}")
    ), title="Puzzles", border_style="green")
    yield Panel.fit(purchase_box(), title="Purchases", border_style="red")


# global variables
already_printed_money_box = False
already_registered_atexit = False


def register_money_box_atexit():
    global already_registered_atexit
    if already_registered_atexit:
        return
    register(print_money_box)
    already_registered_atexit = True


def should_not_print_money_box(already_printed_money_box: bool):
    """
    No need to print the money box if
    - We already printed it (that would be a bit excessive)
    - the user has purchased a code.
    - if stdout is not a tty, that would just
      be rude.
    """
    return already_printed_money_box or have_purchased_code() or not isatty(stdout.fileno())


def print_money_box():
    global already_printed_money_box
    if should_not_print_money_box(already_printed_money_box):
        return

    print(Panel.fit(text_group(),
          title="Puns, Puzzles, and Purchases", border_style="green"))
    already_printed_money_box = True


if __name__ == "__main__":
    print_money_box()
