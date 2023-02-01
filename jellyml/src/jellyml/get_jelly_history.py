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
from .get_jelly_history_path import get_jelly_history_path
from os.path import exists
from .JellyHistoryJSON import JellyHistoryJSON
from .parse_jelly_history import parse_jelly_history
from .Run import Run


def get_jelly_history(run: Run) -> JellyHistoryJSON:
    """
    Gets the jelly history.
    """
    jelly_history_path = get_jelly_history_path(run)
    if not exists(jelly_history_path):
        out: JellyHistoryJSON = {
            "version": "january-07-2023",
            "history_stack": [],
        }
        return out
    try:
        with open(jelly_history_path, "r") as history_fd:
            return parse_jelly_history(history_fd)
    except Exception as e:
        raise Exception(
            f"Failed to parse the jelly history file at {jelly_history_path}") from e
