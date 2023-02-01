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
from .JellyHistoryItem import JellyHistoryItemV1_Pull
from .print_info import print_info


@group()
def text_group(branch_name: str, last_item: JellyHistoryItemV1_Pull):
    yield f"""Successfully undid.

We noticed that you made changes to the snapshot after loading.
If you saved any models with create_snapshot, your changes are
still saved in the jelly-filled models, like usual.

But, just in case, we saved those changes for you in a branch called {branch_name}.
You can look up how to use git branches here: [blue underline]https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell[/[blue underline]
(some terminals may not follow the link)"""

# If you want to go back to your changes (aka redo), run:""")
#     yield ShellCode(f"git checkout {branch_name}")
#     yield Text("and to undo the redo run:")
#     yield ShellCode(f"git checkout {last_item['git_branch_name_or_commit_hash']}")
#     yield Text(f"""the idea is that you can use `git checkout {branch_name}` and `git checkout {last_item['git_branch_name_or_commit_hash']}`
# to switch between the two states.
# One last tidbit for using git checkout, if git complains about the your working tree being dirty, you can run:""")
#     yield ShellCode(f"""git add -A
# git commit -m 'commit message'""")
#     yield Text(f"to commit your changes and then run the checkout command again.")


def print_undo_1(branch_name: str, last_item: JellyHistoryItemV1_Pull):
    print_info(text_group(branch_name, last_item))


if __name__ == "__main__":
    print_undo_1(branch_name="fake_branch_name",
                 last_item={
                     "version": "january-07-2023",
                     "type": "pull",
                     "date": "2021-01-07T00:00:00",
                     "going_to_model_snapshot": "5",
                     "model_snapshot_commit_hash": "5",
                     "git_branch_name_or_commit_hash": "5",
                     "git_stash_message": None,
                 })

    