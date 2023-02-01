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
from .styles import jelly


@group()
def GitLogo():
    yield Text("").join([Text("        ▄███▄", style=jelly)])
    yield Text("").join([Text("      ▄▄▀█████▄", style=jelly)])
    yield Text("").join([Text("    ▄████   ████▄", style=jelly)])
    yield Text("").join([Text("  ▄██████▄ ▄▀█████▄", style=jelly)])
    yield Text("").join([Text(" █████████ ██   ████", style=jelly)])
    yield Text("").join([Text(" ▀████████ ██▄▄▄███▀", style=jelly)])
    yield Text("").join([Text("   ▀█████▀ ▀█████▀", style=jelly)])
    yield Text("").join([Text("     ▀███   ███▀", style=jelly)])
    yield Text("").join([Text("       ▀█████▀", style=jelly)])
    yield Text("").join([Text("         ▀▀▀", style=jelly)])


if __name__ == "__main__":
    from rich import print
    print(GitLogo())
