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
from .get_current_commit_hash import get_current_commit_hash
from typing import Tuple

def get_current_branch_name(run: Run) -> Tuple[str, bool]:
    """
    Returns the name of the current branch or the hash of the current commit if the head is detached,
    Returns true if the head is detached, false otherwise
    """
    current_branch = run.get("git branch --show-current")

    # if current_branch == "": then the head is already detached
    if current_branch == "":
        current_branch = get_current_commit_hash(run)
        return (current_branch, True)
    return (current_branch, False)
