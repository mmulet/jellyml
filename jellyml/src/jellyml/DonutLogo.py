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
from rich.console import Group, group
from rich.table import Table
from rich.text import Text
from rich import print
from typing import Callable
from rich import get_console
from rich.align import Align
from .styles import (frosting, donut, name_over_blank, name_over_donut,
    name_over_frosting, yellow_sprinkle, blue_sprinkle, green_sprinkle,
    dark_magenta_sprinkle, title)

global_donut_logo_enabled = True


def disable_donut_logo():
    global global_donut_logo_enabled
    global_donut_logo_enabled = False


def enable_donut_logo():
    global global_donut_logo_enabled
    global_donut_logo_enabled = True


@group()
def Donut():
    yield Text("").join([Text(" "*12), Text("▓" + "█"*10 + "▓▒░", style=donut), ])
    yield Text("").join([Text(" ┌  ┐ ┬ ┌", style=name_over_blank),
                         Text("▒", style=donut),
                         Text("││", style=name_over_donut),
                         Text("░", style=frosting),
                         Text("┌┐", style=name_over_frosting),
                        Text("█", style=frosting),
                        Text("┌", style=name_over_frosting),
                        Text("█", style=frosting),
                        Text("│", style=name_over_frosting),
                        Text("██▓", style=frosting),
                        Text("┌", style=name_over_frosting),
                        Text("▒▒", style=frosting),
                        Text("┐", style=name_over_frosting),
                        Text("▒", style=frosting),
                         Text("││", style=name_over_donut),
                         Text("░", style=donut),
                        Text("│ ┌ ┬ /", style=name_over_blank),
                         ])
    yield Text("").join([
        Text(" \\\\/│ ", style=name_over_blank),
        Text("│", style=name_over_donut),
        Text("█", style=donut),
        Text("│", style=name_over_donut),
        Text("▓", style=frosting),
        Text("├┤", style=name_over_frosting),
        Text("█", style=frosting),
        Text("├┤", style=name_over_frosting),
        Text("█", style=frosting),
        Text("├", style=name_over_frosting),
        Text("█", style=frosting),
        Text("│", style=name_over_frosting),
        Text("███", style=frosting),
        Text("\\\\/│", style=name_over_frosting),
        Text("█", style=frosting),
        Text("││", style=name_over_frosting),
        Text("█", style=frosting),
        Text("│", style=name_over_donut),
        Text("▒", style=donut),
        Text("├", style=name_over_donut),
        Text(" │  ┌", style=name_over_blank),
    ])

    yield Text("").join([
        Text(" │  │", style=name_over_blank),
        Text("█", style=donut),
        Text("┴", style=name_over_donut),
        Text("▒", style=frosting),
        Text("└", style=name_over_frosting),
        Text("█", style=frosting),
        Text("││", style=name_over_frosting),
        Text("█", style=frosting),
        Text("││", style=name_over_frosting),
        Text("█", style=frosting),
        Text("└", style=name_over_frosting),
        Text("█", style=frosting),
        Text("└", style=name_over_frosting),
        Text("███", style=frosting),
        Text("│", style=name_over_frosting),
        Text("██", style=frosting),
        Text("│", style=name_over_frosting),
        Text("▒", style=frosting),
        Text("└┘", style=name_over_frosting),
        Text("█", style=frosting),
        Text("└", style=name_over_frosting),
        Text("█", style=frosting),
        Text("└", style=name_over_frosting),
        Text("▒", style=donut),
        Text("│", style=name_over_donut),
        Text("  ┘", style=name_over_blank),

    ])

    yield Text("").join([Text(" "*3 + "▒█", style=donut),
                         Text("▒██", style=frosting),
                         Text("█", style=yellow_sprinkle),
                         Text("███", style=frosting),
                         Text("█", style=green_sprinkle),
                         Text("█", style=frosting),
                         Text("█", style=dark_magenta_sprinkle),
                         Text("█", style=frosting),
                         Text("█", style=yellow_sprinkle),
                         Text("▓███", style=frosting),
                         Text("█", style=green_sprinkle),
                         Text("█████", style=frosting),
                         Text("█", style=yellow_sprinkle),
                         Text("█", style=frosting),
                         Text("█", style=green_sprinkle),
                         Text("███▓", style=frosting),
                         Text("▒▒░", style=donut), ])

    yield Text("").join([Text(" "*3 + "▀ ", style=donut),
                         Text("▀ ▀▀▀██", style=frosting),
                         Text("█", style=yellow_sprinkle),
                         Text("██  ", style=frosting),
                         Text("▄ ▄    ", style=title),
                         Text("░░░", style=donut),
                         Text("███▒█", style=frosting),
                         Text("█", style=green_sprinkle),
                         Text("▓▓▒", style=frosting),
                         Text("░░", style=donut), ])

    yield Text("").join([Text("  ▄█████▄ ", style=title),
                         Text("▀", style=green_sprinkle),
                         Text("▀▀   ", style=frosting),
                         Text("█▀ █      ", style=title),
                         Text("░░", style=donut),
                         Text("▒▓█", style=frosting),
                         Text("█", style=blue_sprinkle),
                         Text("███ ", style=frosting),
                         Text("▄ ", style=title),
                         Text("░", style=donut), ])

    yield Text("").join([Text("  ▄  ", style=donut),
                         Text("██  ▄█▀█▄▄ █  █         ", style=title),
                         Text("░ ", style=donut),
                         Text("▀ ", style=dark_magenta_sprinkle),
                         Text("▀  ", style=frosting),
                         Text("█ ", style=title),
                         Text("░", style=donut), ])

    yield Text("").join([Text("███  ", style=donut),
                         Text("██  █   ▄█ █  █  █   ▄█  █ ██  █ ", style=title),
                         Text("░░", style=donut), ])

    yield Text("").join([Text("▒▀ ", style=donut),
                         Text("▄██ ", style=title),
                         Text("▄ ", style=frosting),
                         Text("█▀▀▀▀  █  █  █  ▄█  ██▄▀█  █ ", style=title),
                         Text("▒▒", style=donut), ])

    yield Text("").join([Text(" ▀██▀ ", style=title),
                         Text("▄█▄ ", style=frosting),
                         Text("█▄▄   █  █  █▄█▀  ▄▀██ █  █ ", style=title),
                         Text("▒▒", style=donut), ])

    yield Text("").join([Text("  ▄ ", style=donut),
                         Text("▄█▓██", style=frosting),
                         Text("▄      ", style=blue_sprinkle),
                         Text("▀  ▀ ▄██▀ ▄█▀ ██ █  █ ", style=title),
                         Text("░", style=donut), ])

    yield Text("").join([Text(" ░██", style=donut),
                         Text("▒█", style=frosting),
                         Text("█", style=yellow_sprinkle),
                         Text("██▓██▒░ ", style=frosting),
                         Text("▄▄▄▄███▀  ▀▀ ", style=title),
                         Text("▄ ", style=frosting),
                         Text("▀  █  █▄▄▄", style=title), ])

    yield Text("").join([Text("  ▒██", style=donut),
                         Text("███", style=frosting),
                         Text("█", style=green_sprinkle),
                         Text("█", style=dark_magenta_sprinkle),
                         Text("█", style=frosting),
                         Text("█", style=yellow_sprinkle),
                         Text("█▓ ", style=frosting),
                         Text("▀▀▀      ", style=title),
                         Text("░▓██", style=frosting),
                         Text("█", style=dark_magenta_sprinkle),
                         Text("█", style=frosting),
                         Text("█", style=dark_magenta_sprinkle),
                         Text("█", style=frosting),
                         Text("▄", style=green_sprinkle), ])

    yield Text("").join([Text("   ░▓█", style=donut),
                         Text("░██████", style=frosting),
                         Text("█", style=green_sprinkle),
                         Text("█", style=frosting),
                         Text("█", style=yellow_sprinkle),
                         Text("█"*3, style=frosting),
                         Text("█", style=blue_sprinkle),
                         Text("█", style=frosting),
                         Text("█", style=dark_magenta_sprinkle),
                         Text("█", style=frosting),
                         Text("█", style=yellow_sprinkle),
                         Text("█"*2, style=frosting),
                         Text("█", style=blue_sprinkle),
                         Text("█", style=yellow_sprinkle),
                         Text("██████▓", style=frosting),
                         Text("▒░", style=donut), ])

    yield Text("").join([Text("    ░▒▓", style=donut),
                         Text("█░█", style=frosting),
                         Text("█", style=green_sprinkle),
                         Text("█"*3, style=frosting),
                         Text("█", style=yellow_sprinkle),
                         Text("█"*2, style=frosting),
                         Text("█", style=blue_sprinkle),
                         Text("█"*3, style=frosting),
                         Text("█", style=green_sprinkle),
                         Text("█"*2, style=frosting),
                         Text("█", style=dark_magenta_sprinkle),
                         Text("▓████▓█", style=frosting),
                         Text("▒▒░", style=donut), ])

    yield Text("").join([Text(" "*7 + "░▒▓", style=donut),
                         Text("░▓██████", style=frosting),
                         Text("█", style=yellow_sprinkle),
                         Text("█"*2, style=frosting),
                         Text("█", style=dark_magenta_sprinkle),
                         Text("█"*3, style=frosting),
                         Text("█", style=yellow_sprinkle),
                         Text("█"*4, style=frosting),
                         Text("▓▒░", style=donut), ])

    yield Text("").join([Text(" "*10 + "░▒", style=donut),
                         Text("░░█░▓██████████▒▓", style=frosting),
                         Text("░", style=donut), ])

    yield Text("").join([Text(" "*14 + "░▒▓██████▓▒░", style=donut), ])


def DonutLogo(group: Group):
    if not global_donut_logo_enabled:
        return group
    grid = Table.grid()
    if get_console().width >= 100:
        grid.add_column(width=41)
        grid.add_column()
        grid.add_row(Donut(), group)
        return grid
    grid.add_column()
    grid.add_row(Align.center(Donut()))
    grid.add_row(group)
    return grid


def WithLogo(f: Callable[..., Group]) -> Callable[..., Group]:
    def wrapper(*args, **kwargs):  # type: ignore
        return DonutLogo(f(*args, **kwargs))

    return wrapper  # type: ignore


if __name__ == "__main__":
    print(Donut())
