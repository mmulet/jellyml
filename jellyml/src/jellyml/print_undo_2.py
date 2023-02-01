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
from .JellyHistoryItem import JellyHistoryItemV1_Pull
from .ShellCode import ShellCode
from .print_info import print_info

@group()
def text_group(last_item: JellyHistoryItemV1_Pull):

    yield Text(f"""The HEAD is not pointing to the commit we expect it to. Can't undo.

The commit we expect it to be pointing to is {last_item['git_branch_name_or_commit_hash']}
or a descendent of it.
This means that git repository is in an unexpected state.

In most cases this is an easy fix, just checkout the commit we expect it to be pointing to.
Here's how to fix it:""")
    yield ShellCode(f"""git checkout {last_item['model_snapshot_commit_hash']}
jellyml undo""")
    yield Text("""If git complains about uncommitted changes, then you can do this:""")
    yield ShellCode("""git add  -A
git commit -m "jellyml commit before fixing the git repo""")
    yield Text("""If git can't find the commit, then the commit may have been deleted.
In that case we will have to delete the last history item:""")
    yield ShellCode("jellyml fix delete-last-history-item")


def print_undo_2(last_item: JellyHistoryItemV1_Pull):
    print_info(text_group(last_item))

if __name__ == "__main__":
    print_undo_2(last_item={
        "version": "january-07-2023",
        "type": "pull",
        "date": "2021-01-07T00:00:00",
        "going_to_model_snapshot": "5",
        "model_snapshot_commit_hash": "5",
        "git_branch_name_or_commit_hash": "5",
        "git_stash_message": None,
    })