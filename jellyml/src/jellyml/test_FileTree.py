from subprocess import run
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
from os import walk
import os
from dataclasses import dataclass
from typing import Dict

@dataclass
class FileStatus:
    """The status of a file in the git repo."""
    status: str
    content: str


FileTree = Dict[str, FileStatus]


def get_file_tree(root_path: str, git_repo_path: str) -> FileTree:
    """Get a dictionary of all the files in the directory tree rooted at root_path.
    The keys are the paths to the files relative to root_path.
    The values are the contents of the files.
    """
    file_tree: FileTree = {}
    for dir_path, _, file_names in walk(root_path):
        if ".git" in dir_path:
            continue
        for file_name in file_names:
            file_path = os.path.join(dir_path, file_name)
            with open(file_path, "r") as f:
                content = f.read()
            status = run(f"git status --porcelain {file_path}", shell=True, check=True,
                         capture_output=True, cwd=git_repo_path).stdout.decode('utf-8').strip().split(" ")
            file_tree[file_path[len(root_path) + 1:]
                      ] = FileStatus(status=status[0], content=content)

    return file_tree


def compare_file_trees(expected: FileTree, actual: FileTree, skip_status_check: bool = False):
    """Compare two file trees.
    If they are equal, return None.
    If they are not equal, return a string describing the differences.
    """
    expected_keys = set(expected.keys())
    actual_keys = set(actual.keys())

    if expected_keys != actual_keys:
        raise Exception(
            f"Expected keys: {expected_keys}, Actual keys: {actual_keys}")

    for key in expected_keys:
        if expected[key].content != actual[key].content:
            raise Exception(
                f"File {key} has different content. Expected: {expected[key].content}, Actual: {actual[key].content}")
        if not skip_status_check and expected[key].status != actual[key].status:
            raise Exception(
                f"File {key} has different status. Expected: {expected[key].status}, Actual: {actual[key].status}")
