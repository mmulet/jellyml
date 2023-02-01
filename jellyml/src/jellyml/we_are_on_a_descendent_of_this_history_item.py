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
from .JellyHistoryItem import JellyHistoryItemV1
from .Run import Run


def we_are_on_a_descendent_of_this_history_item(run: Run,
                                                history_item: JellyHistoryItemV1,
                                                current_commit_hash: str) -> bool:
    try:
        # git merge-base --is-ancestor returns 0 if the first commit is an ancestor of the second commit
        # and 1 if it is not
        run.get(
            f"git merge-base --is-ancestor { history_item['model_snapshot_commit_hash']} {current_commit_hash}")
        return True
    except:
        return False
