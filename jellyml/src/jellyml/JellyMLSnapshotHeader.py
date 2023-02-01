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

class JellyMLSnapshotHeaderV1(TypedDict):
    # magic number is used to identify the file as a JellyML file
    magic_number: Literal["jelly_ml_snapshot"]
  
    # snapshot offset is the git bundle, appended to the end of the file,
    # should be the same as padded_header_size_in_bytes
    # offset is from jellyml.beginning of file
    snapshot_offset: int
    # size of the git bundle, appended to the end of the file
    # this does not include the size of the footer
    snapshot_size: int
    version: Literal["january-7-2023"]
  


