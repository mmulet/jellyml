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
from os.path import exists
from json import load
from .JellyMLHistoryMap import JellyMLHistoryMap
from .get_jellyml_history_map_path import get_jellyml_history_map_path


def get_jelly_history_map() -> JellyMLHistoryMap:

    history_map_json_path = get_jellyml_history_map_path()
    if not exists(history_map_json_path):
        with open(history_map_json_path, "w") as history_map_fd:
            history_map_fd.write("{}")
    try:
        with open(history_map_json_path, "r") as history_map_fd:
            return load(history_map_fd)
    except Exception as e:
        raise Exception(
            f"Failed to parse the jelly history map file at {history_map_json_path}") from e
