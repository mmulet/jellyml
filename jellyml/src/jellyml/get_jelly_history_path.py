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
from os.path import join
from json import dump
from uuid import uuid4
from .get_jellyml_history_map import get_jelly_history_map
from .get_jellyml_history_map_path import get_jellyml_history_map_path
from .get_user_data_dir_path import get_user_data_dir_path
from .Run import Run


def get_repo_uuid(git_repo_top_level: str):
    map_json = get_jelly_history_map()
    if git_repo_top_level in map_json:
        return map_json[git_repo_top_level]
    # if it's not it the map, we need to add it
    new_history_file_name = f"{uuid4()}.json"
    map_json[git_repo_top_level] = new_history_file_name
    history_map_json_path = get_jellyml_history_map_path()
    with open(history_map_json_path, "w") as history_map_fd:
        dump(map_json, history_map_fd)

    return new_history_file_name


def get_jelly_history_path_from_git_top_level(git_repo_top_level: str) -> str:
    """
    Gets the path to the jelly history file. Will create the necessary directories if they don't exist. (but not the file itself)
    """
    return join(get_user_data_dir_path(), get_repo_uuid(git_repo_top_level))


def get_jelly_history_path(run: Run) -> str:
    """
    Gets the path to the jelly history file. Will create the necessary directories if they don't exist. (but not the file itself)
    must be called from jellyml.within a git repo.
    """

    git_repo_top_level = run.get("git rev-parse --show-toplevel")

    return get_jelly_history_path_from_git_top_level(git_repo_top_level)
