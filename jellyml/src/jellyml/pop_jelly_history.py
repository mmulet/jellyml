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
from .JellyHistoryItem import JellyHistoryItem
from .JellyHistoryJSON import JellyHistoryJSON
from .write_jelly_history import write_jelly_history
from .HistoryFd import HistoryFd
from .Run import Run


def pop_jelly_history(run: Run, jelly_history: JellyHistoryJSON) -> JellyHistoryItem:
    """
    pop the last jelly history item
    """
    if len(jelly_history['history_stack']) <= 0:
        raise Exception("There is nothing to pop")
    with HistoryFd(run, "w") as history_fd:
        old = jelly_history['history_stack'].pop()
        write_jelly_history(jelly_history, history_fd)
        return old
