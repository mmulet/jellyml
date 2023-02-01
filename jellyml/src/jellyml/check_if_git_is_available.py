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
from subprocess import run
from .print_info import print_info
from rich.console import Group, group
from .GitLogo import GitLogo
from rich.panel import Panel
from rich.table import Table


@group()
def text_group():
    yield """Git is not installed.
You don't need to know how to use git to use jellyml, but it does need be installed.
Please install git to use jellyml."""
    table = Table.grid(expand=True)
    table.add_column(ratio=1, width=21)
    table.add_column(vertical="middle", ratio=2)
    table.add_row(GitLogo(), Group("download git from",
                  "[blue underline]https://git-scm.com/downloads[/blue underline]\n(some terminals may not follow links)" ))
    yield Panel.fit(Group(table, "Git Logo by Jason Long is licensed under the Creative Commons Attribution 3.0 Unported License.\nANSI art by me."), title="git", border_style="red")
    yield """If you just installed git, please restart your terminal.\n"""


def check_if_git_is_available():
    # check if git is available
    try:
        run("git --version", check=True, shell=True,
            capture_output=True)
        return True
    except:
        print_info(text_group())
        exit(1)


if __name__ == "__main__":
    print_info(text_group())
