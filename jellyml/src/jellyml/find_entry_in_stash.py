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
from typing import Optional


def find_entry_in_stash(run: Run, message: str) -> Optional[str]:
    lines = run.get("git stash list").split("\n")
    lines = [line for line in lines if len(line) > 0]
    for line in lines:
        entries = line.split(" ")
        line_message = entries[-1]
        if message != line_message:
            continue
        stash_id = entries[0]
        if stash_id.endswith(":"):
            stash_id = stash_id[:-1]
        return stash_id
    return None
