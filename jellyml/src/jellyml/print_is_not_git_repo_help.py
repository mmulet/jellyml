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
from rich.console import group
from rich.text import Text
from .ShellCode import ShellCode
from .print_info import print_info
from rich.syntax import Syntax
from .Run import Run
from typing import Optional

def print_is_not_git_repo_help(run: Run, out_git_bundle_path: Optional[str]):
    @group()
    def text_group():
        actual_path = run.get_working_directory_path()
        yield Text(f"""The directory {actual_path} is not a git repository.
    So, we can't create a snapshot of your code.\n
    If you want jellyml to create a .gitignore file and a git repository for you, you can change your function call to:
    """)
        repo_path_args = run.get_repo_path_args()
        out_git_bundle_path_args = "" if out_git_bundle_path is None else f"out_git_bundle_path={out_git_bundle_path},"
        yield Panel.fit(Syntax(f"""import jellyml
snapshot = jellyml.create_snapshot({repo_path_args}{out_git_bundle_path_args}create_git_repo=True)
""", "python", line_numbers=True),
                        title="python",
                        border_style="yellow")
       
        
        yield f"""This will create a git repo at {actual_path},
 meaning everything inside {actual_path} will be saved to the snapshot.
 It will also create a .gitignore file."""
       
        yield "\nOr you can create a .gitignore manually then use the following command to create the repository:"
        yield ShellCode("git init")

    print_info(text_group())

if __name__ == "__main__":
    print_is_not_git_repo_help(Run(git_repo_path=None), None)