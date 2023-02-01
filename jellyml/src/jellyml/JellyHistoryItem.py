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
from typing_extensions import TypedDict, Literal
from typing import Optional, Union


class JellyHistoryItemV1_base_incomplete(TypedDict):
    version: Literal["january-07-2023"]
    date: str
    going_to_model_snapshot: str

class JellyHistoryItemV1_base(JellyHistoryItemV1_base_incomplete):
    model_snapshot_commit_hash: str


class JellyHistoryItemV1_Clone(JellyHistoryItemV1_base):
    version: Literal["january-07-2023"]
    type: Literal["clone"]
    date: str
    going_to_model_snapshot: str


class JellyHistoryItemV1_Pull(JellyHistoryItemV1_base):
    """
    It's actually a fetch and checkout, not a pull in git terms (a fetch and merge),
    but pull is only 4 letters, so it's easier to type.
    """
    type: Literal["pull"]
    git_branch_name_or_commit_hash: str
    git_stash_message: Optional[str]


JellyHistoryItemV1 = Union[JellyHistoryItemV1_Clone, JellyHistoryItemV1_Pull]


# will be a union of all versions
JellyHistoryItem = JellyHistoryItemV1
