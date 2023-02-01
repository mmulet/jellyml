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
from .styles import (donut, frosting, blue_sprinkle, green_sprinkle,
                     yellow_sprinkle, construction, purple_sprinkle, jelly, jelly_on_construction)


@ group()
def SecretAward():
    yield Text("").join([Text("           ▄▒▓██▓██▓░░▒▒▒▒░░░████████▄", style=donut)])
    yield Text("").join([Text("  ▓▒▀▀▓▓▓▓▒█████░░░▒", style=donut),
                         Text("██", style=frosting),
                         Text("█", style=blue_sprinkle),
                         Text("█"*3, style=frosting),
                         Text("█", style=purple_sprinkle),
                         Text("██", style=frosting),
                         Text("▒░░███████▓▓▀▀██▓", style=donut)
                         ])
    yield Text("").join([
        Text(" ▓▓▒   ▓░▓▓████░▒", style=donut),
        Text("█"*4, style=frosting),
        Text("█", style=yellow_sprinkle),
        Text("█"*2, style=frosting),
        Text("█", style=green_sprinkle),
        Text("█"*2, style=frosting),
        Text("█", style=blue_sprinkle),
        Text("██▓", style=frosting),
        Text("▒░██████▓    █▓▓", style=donut),
    ])

    yield Text("").join([
        Text(" ▓▓▓     ▓▓▓▓█░▒", style=donut),
        Text("█"*2, style=frosting),
        Text("█", style=green_sprinkle),
        Text("█", style=frosting),
        Text("█", style=purple_sprinkle),
        Text("█"*4, style=frosting),
        Text("█", style=yellow_sprinkle),
        Text("███", style=frosting),
        Text("█", style=green_sprinkle),
        Text("██", style=frosting),
        Text("▒░███▓▓     ███", style=donut),
    ])

    yield Text("").join([
        Text(" ▓███     ▓█▓░▒", style=donut),
        Text("█", style=blue_sprinkle),
        Text("█", style=frosting),
        Text("█", style=yellow_sprinkle),
        Text("█"*3, style=frosting),
        Text("░░░░░░", style=donut),
        Text("▓█", style=frosting),
        Text("█", style=blue_sprinkle),
        Text("█", style=frosting),
        Text("█", style=blue_sprinkle),
        Text("█", style=frosting),
        Text("▒░█▓▓      ▓█▒", style=donut),
    ])

    yield Text("").join([
        Text(" ▒▒▓█░    ▒▓░▒", style=donut),
        Text("█"*4, style=frosting),
        Text("█", style=blue_sprinkle),

        Text("█", style=frosting),
        Text("░░    ░░", style=donut),
        Text("█"*4, style=frosting),
        Text("█", style=purple_sprinkle),
        Text("█", style=frosting),
        Text("▒░█▓    ▓▓▓▒▒", style=donut),
    ])

    yield Text("").join([
        Text("  ▒▓▓▓██ ▄▓▓░▒", style=donut),
        Text("█", style=purple_sprinkle),
        Text("█", style=frosting),
        Text("█", style=green_sprinkle),
        Text("█▓", style=frosting),
        Text("░░      ░░", style=donut),
        Text("▓", style=frosting),
        Text("█", style=blue_sprinkle),
        Text("█▓▒", style=frosting),
        Text("▒░██ ▄████▒▒  ", style=donut),
        Text("██", style=jelly),
        Text("▒ ", style=construction),
        Text("██", style=jelly),
        Text("▒", style=construction),
    ])
    yield Text("").join([
        Text("    ▒▓▓▓▓▓▓█░▒", style=donut),
        Text("█", style=frosting),
        Text("█", style=blue_sprinkle),
        Text("█"*2, style=frosting),
        Text("█", style=blue_sprinkle),
        Text("░", style=frosting),
        Text("░      ░", style=donut),
        Text("█"*3, style=frosting),
        Text("█", style=green_sprinkle),
        Text("█"*2, style=frosting),
        Text("▒░██▓▓▓▓▓     ", style=donut),

        Text("██", style=jelly),
        Text("▒ ", style=construction),
        Text("██", style=jelly),
        Text("▒", style=construction),

        Text("▄█▀█", style=jelly),
        Text("▄", style=jelly_on_construction),
        Text("▄", style=construction),
        Text("██ ██", style=jelly),
        Text("░", style=construction),
    ])
    yield Text("").join([
        Text(" "*5 + "▒▓▓▓▓▓▓█░▒▒", style=donut),
        Text("▓███░", style=frosting),
        Text("░░░░░░", style=donut),
        Text("▒", style=frosting),
        Text("█", style=yellow_sprinkle),
        Text("██▒▒", style=frosting),
        Text("▒░██████▓" + " "*7, style=donut),
        Text("▀██", style=jelly),
        Text("▒▀ ", style=construction),
        Text("██ ██", style=jelly),
        Text("▒", style=construction),
        Text("██ ██", style=jelly),
        Text("░", style=construction),





    ])

    yield Text("").join([
        Text(" "*7 + "▒▓▓▓███░▒", style=donut),
        Text("▓▒", style=frosting),
        Text("█", style=blue_sprinkle),
        Text("▓▓▓", style=frosting),
        Text("█", style=yellow_sprinkle),
        Text("▓▓▓▓", style=frosting),
        Text("█", style=purple_sprinkle),
        Text("▓█", style=frosting),
        Text("█", style=blue_sprinkle),
        Text("░", style=frosting),
        Text("▒░█████▓" + " "*10, style=donut),
        Text("██", style=jelly),
        Text("▒  ", style=construction),
        Text("▀█▄█", style=jelly),
        Text("▒▀", style=construction),
        Text("▀█▄██", style=jelly),
        Text("░", style=construction),
    ])
    yield Text("").join([
        Text(" "*9 + "▓█████░▒", style=donut),
        Text("█", style=yellow_sprinkle),
        Text("██", style=frosting),
        Text("█", style=green_sprinkle),
        Text("▓██", style=frosting),
        Text("█", style=blue_sprinkle),
        Text("█", style=frosting),
        Text("█", style=yellow_sprinkle),
        Text("██▒░", style=frosting),
        Text("▒░████▓" + " "*13, style=donut),
        Text("▀▀" + " "*4 + "▀▀▀" + "   " + "▀▀▀▀", style=construction),
    ])
    yield Text("").join([
        Text(" "*12 + "▓████░▒▒", style=donut),
        Text("░▒▓██", style=frosting),
        Text("█", style=blue_sprinkle),
        Text("▒░", style=frosting),
        Text("▒▒░████▓" + " "*9, style=donut),
        # Text("▀▀" + " "*4 + "▀▀▀" + "   " + "▀▀▀▀", style=construction),
        # Text("▀▀" + " "*4 + "▀▀▀" + "   " + "▀▀▀▀", style=construction),

        Text("██", style=jelly),
        Text("▒", style=construction),
        Text("▀▀", style=jelly),
        Text("▀   ", style=construction),
        Text("██", style=jelly),
        Text("▒  ", style=construction),
        Text("▀▀", style=jelly),
        Text("▀ ", style=construction),
        Text("██", style=jelly),
        Text("▒  ", style=construction),
    ])
    yield Text("").join([
        Text(" "*17 + "██▒▒▒▒▒▒▒▒▒▒░█" + " "*11, style=donut),
        Text("▄█▀██", style=jelly),
        Text("▒", style=construction),
        Text("██", style=jelly),
        Text("▒", style=construction),
        Text("▄█▀██", style=jelly),
        Text("▒  ", style=construction),
        Text("██", style=jelly),
        Text("▒", style=construction),
        Text("▀██", style=jelly),
        Text("▀", style=jelly_on_construction),
        Text("▀", style=construction),
    ])
    yield Text("").join([
        Text(" "*17 + "████░░░░░█████" + " "*11, style=donut),
        Text("██ ██", style=jelly),
        Text("▒", style=construction),
        Text("██", style=jelly),
        Text("▒", style=construction),
        Text("██ ██", style=jelly),
        Text("▒  ", style=construction),
        Text("██", style=jelly),
        Text("▒ ", style=construction),
        Text("██", style=jelly),
        Text("▒", style=construction),
    ])
    yield Text("").join([
        Text(" "*17 + "▓▓▓▓▓▓▓▓▓▓▓▓▓▓" + " "*11, style=donut),
        Text("▀█▄██", style=jelly),
        Text("▒", style=construction),
        Text("██", style=jelly),
        Text("▒", style=construction),
        Text("▀█▄██", style=jelly),
        Text("▒  ", style=construction),
        Text("██", style=jelly),
        Text("▒ ", style=construction),
        Text("▀█", style=jelly),
        Text("▄", style=jelly_on_construction),
        Text("▄", style=construction),
    ])
    yield Text("").join([
        Text(" "*19 + "▓████████▓" + " "*15, style=donut),
        Text("▀▀▀▀ ▀▀  ▀▀▀▀   ▀▀   ▀▀", style=construction),
    ])
    yield Text("").join([
        Text(" "*13 + "▒▒▒▒▓", style=construction),
        Text("▓██████████▓", style=donut),
        Text("▓░██▓█▓", style=construction),
    ])
    yield Text("").join([
        Text(" "*7 + "▒▒▒▒█▓█▓", style=construction),
        Text("▓████████████████▓", style=donut),
        Text("████▓", style=construction),
    ])
    yield Text("").join([
        Text(" "*7 + "▄▄▄", style=jelly),
        Text("▄" + " "*31, style=construction),
        Text("▄▄", style=jelly),
        Text("▄" + " "*6, style=construction),
        Text("▄▄", style=jelly),
        Text("▄", style=construction),
        Text("▄▄", style=jelly),
        Text("▄", style=construction),
        Text("▄▄", style=jelly),
        Text("▄", style=construction),
    ])
    yield Text("").join([
        Text(" "*6 + "██", style=jelly),
        Text("░▀", style=construction),
        Text("▀", style=jelly),
        Text("▀ ", style=construction),
        Text("▄▄▄", style=jelly),
        Text("▄ ", style=construction),
        Text("▄▄▄▄", style=jelly),
        Text("▄  ", style=construction),
        Text("▄▄▄▄", style=jelly),
        Text("▄", style=construction),
        Text("▄▄ ▄", style=jelly),
        Text("▄ ", style=construction),
        Text("▄▄▄", style=jelly),
        Text("▄ ", style=construction),
        Text("▄██", style=jelly),
        Text("▄", style=jelly_on_construction),
        Text("▄ ", style=construction),
        Text("▄▄", style=jelly),
        Text("▄ ", style=construction),
        Text("██", style=jelly),
        Text("░", style=construction),
        Text("██", style=jelly),
        Text("░", style=construction),
        Text("██", style=jelly),
        Text("░", style=construction),
    ])

    yield Text("").join([
        Text(" "*6 + "██", style=jelly),
        Text("░   ", style=construction),
        Text("██ ██", style=jelly),
        Text("░", style=construction),
        Text("██ ██", style=jelly),
        Text("░", style=construction),
        Text("██ ██", style=jelly),
        Text("░", style=construction),

        Text("██", style=jelly),
        Text("▀▀", style=jelly_on_construction),
        Text("▀", style=construction),
        Text("▀  ██", style=jelly),
        Text("░ ", style=construction),
        Text("██", style=jelly),
        Text("░ ", style=construction),
        Text("██▄", style=jelly),
        Text("▀", style=jelly_on_construction),
        Text("▀", style=construction),
        Text("██", style=jelly),
        Text("░", style=construction),
        Text("██", style=jelly),
        Text("░", style=construction),
        Text("██", style=jelly),
        Text("░", style=construction),

    ])
    yield Text("").join([
        Text(" "*6 + "██", style=jelly),
        Text("░▄", style=construction),
        Text("▄", style=jelly),
        Text("▄", style=construction),
        Text("██ ██", style=jelly),
        Text("░", style=construction),
        Text("██ ██", style=jelly),
        Text("░", style=construction),
        Text("██ ██", style=jelly),
        Text("░", style=construction),
        Text("██", style=jelly),
        Text("░  ", style=construction),
        Text("▄█▀██", style=jelly),
        Text("░ ", style=construction),
        Text("██", style=jelly),
        Text("░ ", style=construction),
        Text("▄▀██", style=jelly),
        Text("█", style=construction),
        Text("▄▄", style=jelly),
        Text("▄", style=construction),
        Text("▄▄", style=jelly),
        Text("▄", style=construction),
        Text("▄▄", style=jelly),
        Text("▄", style=construction),
    ])
    yield Text("").join([
        Text(" "*7 + "▀", style=jelly),
        Text("▀▀", style=jelly_on_construction),
        Text("░  ", style=construction),
        Text("▀", style=jelly),
        Text("▀▀", style=jelly_on_construction),
        Text("░ ", style=construction),
        Text("▀", style=jelly),
        Text("▀", style=jelly_on_construction),
        Text("▄", style=construction),
        Text("▀▀", style=jelly_on_construction),
        Text("▀", style=construction),
        Text("▄▀▀██", style=jelly),
        Text("░", style=construction),
        Text("▀", style=jelly),
        Text("▀", style=jelly_on_construction),
        Text("░   ", style=construction),
        Text("▀", style=jelly),
        Text("▀▀▀", style=jelly_on_construction),
        Text("░  ", style=construction),
        Text("▀", style=jelly),
        Text("▀", style=jelly_on_construction),
        Text("░ ", style=construction),
        Text("▀", style=jelly),
        Text("▀", style=jelly_on_construction),
        Text("▀ ", style=construction),

        Text("▀", style=jelly),
        Text("▀", style=jelly_on_construction),
        Text("░", style=construction),
        Text("▀", style=jelly),
        Text("▀", style=jelly_on_construction),
        Text("░", style=construction),
        Text("▀", style=jelly),
        Text("▀", style=jelly_on_construction),
        Text("░", style=construction),
    ])

    yield Text("").join([
        Text(" "*25 + "▀", style=jelly),
        Text("▀▀▀", style=jelly_on_construction),
        Text("▀", style=construction),
    ])


if __name__ == "__main__":
    from rich import print
    print(SecretAward())
