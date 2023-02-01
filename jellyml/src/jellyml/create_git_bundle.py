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
from .Run import Run
from datetime import datetime
from .get_current_branch_name import get_current_branch_name
from .working_tree_is_clean import working_tree_is_clean
from uuid import uuid4


def create_git_bundle(run: Run, bundle_path: str):

    def make_bundle():
        run(f"git bundle create --quiet {bundle_path} HEAD")

    # if working tree is clean, just create a bundle
    # don't have to deal with the stash or detaching or anything
    if working_tree_is_clean(run):
        make_bundle()
        return

    # Working tree is dirty so we are going to create
    # a new commit with the current changes committed to it
    # and make a bundle out of that
    run("git stash --include-untracked --quiet")
    current_branch, head_is_detached = get_current_branch_name(
        run)
    if not head_is_detached:
        # detach the head
        run(f"git checkout --detach --quiet")

    new_branch_message = f"jellyml_snapshot_at_{datetime.now().date()}-{uuid4()}"
    # apply the stash but keep the changes in the stack (doesn't pop)
    run("git stash apply --quiet")
    run("git add -A")
    run(f"git commit --quiet -m '{new_branch_message}' ")

    make_bundle()

    run(f"git checkout --quiet {current_branch}")
    # restore the working directory to the state it was before
    # and remove the stash from jellyml.the stack
    run("git stash pop --quiet")
