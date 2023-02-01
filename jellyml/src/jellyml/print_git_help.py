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
from .ShellCode import ShellCode
from .print_info import print_info
from .GitLogo import GitLogo
from rich.panel import Panel
from rich.table import Table


@group()
def text_group():

    table = Table.grid(expand=True)
    table.add_column()
    table.add_column(vertical="middle")
    table.add_row(
        GitLogo(), "usage: jellyml git path_to_model_file [git_args with {} replaced]\n")
    yield Panel.fit(Group(table, "Git Logo by Jason Long is licensed under the Creative Commons Attribution 3.0 Unported License.\nANSI art by me."), title="git")

    yield Text(" Forward the rest of the arguments to git using the model file as the git repo.\n")

    yield Text(" {} will be replaced as the path to the git repo\n", style="bold")
    yield Text("For example, change:\n")
    yield ShellCode("git clone jellyml.com/my_repo.git\n")
    yield Text(" to:\n")
    yield ShellCode("jellyml git model_file.pt clone {}\n")
    yield Text(" More examples:\n")
    yield ShellCode("jellyml git model_file.pt fetch {}\n")
    yield ShellCode("jellyml git model_file.pt checkout {}\n")


def print_git_help():
    print_info(text_group())


if __name__ == "__main__":
    print_git_help()
