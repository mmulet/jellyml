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
from json import dump
from typing_extensions import Any
from typing import IO
from .JellyHistoryJSON import  JellyHistoryJSON

def write_jelly_history(history: JellyHistoryJSON, history_fd: IO[Any]):
    """
    Writes the history file json.
    """
    history_fd.seek(0)
    history_fd.truncate()
    dump(history, history_fd)
    history_fd.flush()