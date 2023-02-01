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
from .test_project_root_directory import project_root_directory
from shutil import rmtree
from os.path import join
from atexit import register
from .fix_clear_history import clear_history, ClearHistoryArgs_dataclass
from os import makedirs
from subprocess import run
from rich.traceback import install
from .test_FileTree import get_file_tree
from ._create_snapshot import create_snapshot
import torch

install(show_locals=True)


class TestRepo:
    def __init__(self) -> None:
        self.path = join(
            project_root_directory, 'tests', 'test_git_repo')
        self.output_path = join(
            project_root_directory, 'tests', 'test_output')

        def remove_test_git_repo():
            rmtree(self.path, ignore_errors=True)
            rmtree(self.output_path, ignore_errors=True)
            clear_history(ClearHistoryArgs_dataclass(self.path))

        register(remove_test_git_repo)
        # start with a clean slate
        remove_test_git_repo()
        makedirs(self.path)
        makedirs(self.output_path, exist_ok=True)
        run('git init --quiet', shell=True, cwd=self.path, check=True)

    def run(self, s: str):
        run(s, shell=True, cwd=self.path, check=True)

    def run_with_output(self, s: str):
        return run(s, shell=True, cwd=self.path, check=True,
                   capture_output=True).stdout.decode('utf-8').strip()

    def join(self, *args: str):
        return join(self.path, *args)  # type: ignore

    def write_to_file(self, path: str, contents: str):
        with open(self.join(path), 'w') as f:
            f.write(contents)

    def get_file_tree(self):
        return get_file_tree(self.path, git_repo_path=self.path)

    def save_snapshot_to_tensor(self, tensor_name: str) -> str:
        """
        save snapshot to tensor.pt
        and returns the path to the tensor
        """
        snapshot = create_snapshot(git_repo_path=self.path)
        tensor=torch.tensor([1, 2, 3])
        tensor_path=join(self.output_path, tensor_name)
        torch.save({  # type: ignore
            'data': tensor,
            **snapshot
        }, tensor_path)
        return tensor_path
