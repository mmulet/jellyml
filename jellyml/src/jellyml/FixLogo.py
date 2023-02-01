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
from rich.console import group
from rich.text import Text
from rich.style import Style
from .styles import (donut, frosting, frosting_on_donut, blue_sprinkle, green_sprinkle,
                     construction_color, yellow_sprinkle, construction, construction_2,
                     )


@ group()
def FixLogo():
    yield Text("").join([Text("    ▄▀▄ ▄▀ █      █ ", style=construction)])
    yield Text("").join([Text("  ▄▀▄ ▄▀   █", style=construction),
                         Text("▄▄    ", style=donut),
                         Text("▓ ", style=construction),

                         ])
    yield Text("").join([Text("▄▀▄ ▄▀     █", style=construction),
                         Text("▄", style=blue_sprinkle),
                         Text("▄ ", style=frosting_on_donut),
                         Text("▒░ ", style=donut),
                         Text("▒", style=construction),
                         ])
    yield Text("").join([Text("▄ ▄▀       █", style=construction),
                         Text("█", style=frosting),
                         Text("▄", style=blue_sprinkle),
                         Text("█", style=frosting),
                         Text("▄", style=green_sprinkle),
                         Text("▄", style=frosting_on_donut),
                         Text("░", style=donut),
                         Text("▒", style=construction),
                         ])
    yield Text("").join([Text("▄▀         ", style=construction),
                         Text("▀▀▀▀▀▀▀▀", style=construction_2),
                         ])
    yield Text("").join([Text(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄", style=construction),
                         ])
    yield Text("").join([Text(" █", style=construction),
                         Text("▒", style=donut),
                         Text("█", style=frosting),
                         Text("▄", style=Style(color="blue", bgcolor="green")),
                         Text("█   █   █", style=construction),
                         Text("█", style=frosting),
                         Text("▄", style=yellow_sprinkle),
                         Text("▀", style=green_sprinkle),
                        Text("▓", style=construction),
                         ])
    yield Text("").join([Text(" █▄", style=construction),
                         Text("▀", style=Style(color="green",
                              bgcolor=construction_color)),
                         Text("▀", style=Style(color="magenta",
                              bgcolor=construction_color)),
                         Text("█▄▄▄█▄▄▄▓", style=construction),
                         Text("▀", style=Style(color="magenta",
                                               bgcolor=construction_color)),
                         Text("▀", style=Style(color="blue",
                                               bgcolor=construction_color)),
                         Text("▀", style=Style(color="magenta",
                                               bgcolor=construction_color)),
                        Text("▒", style=construction),
                         ])
    yield Text("").join([Text(" █ ", style=construction),
                         Text("░", style=donut),
                         Text("█", style=frosting),
                         Text("█", style=construction),
                         Text("▄", style=green_sprinkle),
                         Text("▄▄", style=frosting),
                         Text("▓ ", style=construction),
                         Text("▄▄", style=frosting),
                         Text("▒", style=construction),
                         Text("▀", style=green_sprinkle),
                         Text("█", style=frosting),
                         Text("░", style=donut),
                         Text("▒ ", style=construction),
                         ])
    yield Text("").join([Text(" █▄▄▄▓", style=construction),
                         Text("▀", style=Style(color="dark_magenta",
                                               bgcolor=construction_color)),
                        Text("▀▀", style=Style(color="magenta",
                                               bgcolor=construction_color)),
                         Text("▒", style=construction),
                         Text("▀▀", style=Style(color="magenta",
                                                bgcolor=construction_color)),
                         Text("▀", style=Style(color="blue",
                                               bgcolor=construction_color)),
                        Text("▒", style=construction),
                         Text("▀", style=Style(color="yellow",
                                               bgcolor=construction_color)),
                        Text("▄▄░", style=construction),
                         ])
    yield Text("").join([Text(" █   ▒ ", style=construction),
                         Text("░", style=donut),
                         Text("▀", style=frosting_on_donut),
                         Text("░", style=construction),
                         Text("▀▀", style=Style(color="magenta",
                                                bgcolor=construction_color)),
                         Text("░", style=donut),
                         Text("░   ░", style=construction),
                         ])


if __name__ == "__main__":
    from rich import print
    print(FixLogo())
