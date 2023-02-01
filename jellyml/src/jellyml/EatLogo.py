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
from .styles import (donut, frosting, frosting_on_donut, blue_sprinkle,
                     green_sprinkle, purple_sprinkle, yellow_sprinkle,
                     jelly, jelly_on_frosting)


@ group()
def EatLogo():
    yield Text("").join([Text("      ▒██████▓", style=donut)])
    yield Text("").join([Text("   █", style=donut),
                         Text("▄▄▄", style=frosting_on_donut),
                         Text("█", style=frosting),
                         Text("▄", style=blue_sprinkle),
                         Text("█", style=frosting),
                         Text("▀", style=green_sprinkle),
                         Text("███▄", style=frosting_on_donut),
                         Text("▒░", style=donut),
                         ])
    yield Text("").join([Text("  ▓", style=donut),
                         Text("██", style=frosting),
                         Text("▀", style=blue_sprinkle),
                         Text("▄", style=purple_sprinkle),
                         Text("█", style=frosting),
                         Text("▄", style=green_sprinkle),
                         Text("█", style=frosting),
                         Text("▀", style=purple_sprinkle),
                         Text("██", style=frosting),
                         Text("▄", style=blue_sprinkle),
                         Text("█", style=frosting),
                         Text("▀", style=yellow_sprinkle),
                         Text("░░", style=donut),
                         ])
    yield Text("").join([Text("    ▀██      ", style=frosting),
                        Text("▄", style=yellow_sprinkle),
                         Text("▀", style=green_sprinkle),
                         Text("█▓", style=frosting),
                         Text("░░", style=donut),
                         ])
    yield Text("").join([Text(" "*14 + "█", style=frosting),
                        Text("▄", style=blue_sprinkle),
                         Text("▓▓", style=frosting),
                         Text("░░", style=donut),
                         ])
    yield Text("").join([Text(" "*15 + "██", style=frosting),
                         Text("▄", style=green_sprinkle),
                         Text("▒▒", style=donut),
                         ])
    yield Text("").join([Text("   ▄▄▄████████", style=jelly),
                         Text("▀", style=jelly_on_frosting),
                         Text("██", style=frosting),
                         Text("▄", style=green_sprinkle),
                         Text("░░", style=donut),
                         ])
    yield Text("").join([Text(" ▄███", style=jelly),
                         Text("█", style=frosting),
                         Text("▄", style=yellow_sprinkle),
                         Text("██████", style=jelly),
                         Text("█", style=frosting),
                         Text("▀▄", style=blue_sprinkle),
                         Text("█", style=frosting),
                         Text("░░", style=donut),
                         ])
    yield Text("").join([Text(" █", style=jelly),
                         Text("▒░", style=donut),
                         Text("▒█", style=frosting),
                         Text("▄", style=blue_sprinkle),
                         Text("█", style=frosting),
                         Text("▀", style=purple_sprinkle),
                         Text("█", style=frosting),
                         Text("▄", style=yellow_sprinkle),
                         Text("██", style=frosting),
                         Text("▄", style=blue_sprinkle),
                         Text("▓▒", style=frosting),
                         Text("░░", style=donut),
                         ])
    yield Text("").join([Text(" █ ", style=jelly),
                         Text("░▒▓▓", style=donut),
                         Text("█", style=frosting),
                         Text("▀", style=purple_sprinkle),
                         Text("▄", style=green_sprinkle),
                         Text("█", style=frosting),
                         Text("▄▀", style=purple_sprinkle),
                         Text("▓▓▒░", style=donut),
                         ])
    yield Text("").join([Text(" █    ", style=jelly),
                         Text("░▒▓██▓▒░", style=donut),
                         ])


if __name__ == "__main__":
    from rich import print
    print(EatLogo())
