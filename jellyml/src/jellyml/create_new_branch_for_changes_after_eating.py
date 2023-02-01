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
from .get_current_commit_hash import get_current_commit_hash
from .JellyHistoryItem import JellyHistoryItemV1_Pull
from datetime import datetime
from .we_are_on_a_descendent_of_this_history_item import we_are_on_a_descendent_of_this_history_item
from .print_undo_1 import print_undo_1
from .print_undo_2 import print_undo_2
from uuid import uuid4
from .get_current_commit_hash import get_current_commit_hash
from sys import stderr
from .working_tree_is_clean import working_tree_is_clean
from .Run import Run
from typing import Optional
from .we_are_in_detached_head import we_are_in_detached_head

def create_new_branch_for_changes_after_eating(run: Run,
                                               last_item: JellyHistoryItemV1_Pull,
                                               quiet: bool) -> Optional[str]:
    """Create a new branch for changes after eating."""

    current_commit_hash = get_current_commit_hash(run)

    current_working_tree_is_clean = working_tree_is_clean(
        run)

    if current_commit_hash == last_item['model_snapshot_commit_hash'] and current_working_tree_is_clean:
        return None
    if not we_are_on_a_descendent_of_this_history_item(run,
                                                       history_item=last_item,
                                                       current_commit_hash=current_commit_hash):
        if quiet:
            print(
                """The HEAD is not pointing to the commit we expect it to. Can't undo.""", file=stderr)
        else:
            print_undo_2(last_item=last_item)
        exit(-1)
    if current_working_tree_is_clean and not we_are_in_detached_head(run):
        # if the working tree is clean, there are no changes to commit
        # and if we are not in detached head, that means the user has already
        # created a branch for the changes they want to keep, no need to create
        # another one
        return None

    branch_name = f"jellyml-undo-{datetime.now().date()}-{uuid4()}"
    run(f"git checkout --quiet -b  {branch_name}")

    if not current_working_tree_is_clean:
        run("git add -A")
        commit_message = f"jellyml commit before undoing from jellyml.snapshot {last_item['going_to_model_snapshot']}"
        run(
            f"git commit --quiet -m '{commit_message}'")
    if not quiet:
        print_undo_1(branch_name=branch_name, last_item=last_item)
    return branch_name
