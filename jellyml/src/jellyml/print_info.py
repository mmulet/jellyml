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
from rich.panel import Panel
from .DonutLogo import DonutLogo
from rich.console import Group
from rich.text import Text
from rich import print

def print_info_message(message: str):
    print(Panel.fit(DonutLogo(Group(Text(message))),
          title="info", border_style="blue"))

def print_info(group: Group):
    print(Panel.fit(DonutLogo(group),
          title="info", border_style="blue"))
