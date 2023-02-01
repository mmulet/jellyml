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

import torch
from .create_git_bundle import create_git_bundle
from .generate_temporary_bundle_path import generate_temporary_bundle_path
from .JellyMLSnapshotHeader import JellyMLSnapshotHeaderV1
from json import dumps
from .constants import padded_header_size_in_bytes, jellyml_dictionary_key
from .is_git_repository import is_git_repository
from .print_is_not_git_repo_help import print_is_not_git_repo_help
from .create_git_repo import create_git_repo as create_git_repo_func
from .print_money_box import register_money_box_atexit
from .Run import Run
from typing import Optional


def create_snapshot(git_repo_path: Optional[str] = None,
                    out_git_bundle_path: Optional[str] = None,
                    create_git_repo: bool = False):
    """
    git_repo_path:  The path to the git repo that we will snapshot, default is os.getcwd()
    git_bundle_path: The path to the temporary git bundle to create, default 
                    is a random path in the system temp directory
    create_git_repo: If True, then create a git repo in the current directory, if there is not one already
    """
    register_money_box_atexit()
    run = Run(git_repo_path=git_repo_path)

    if not is_git_repository(run):
        if not create_git_repo:
            print_is_not_git_repo_help(
                run,
                out_git_bundle_path=out_git_bundle_path)
            raise Exception("The given path is not a git repo")
        create_git_repo_func(run)
    git_bundle_path = out_git_bundle_path if out_git_bundle_path is not None else generate_temporary_bundle_path()
    create_git_bundle(run,
                      bundle_path=git_bundle_path,
                      )
    with open(git_bundle_path, 'rb') as f:
        bundle = f.read()
    header: JellyMLSnapshotHeaderV1 = {'magic_number': "jelly_ml_snapshot",
                                       'snapshot_offset': padded_header_size_in_bytes,
                                       'snapshot_size': len(bundle),
                                       'version': "january-7-2023"}
    header_bytes = dumps(header).encode('utf-8')
    assert len(
        header_bytes) <= padded_header_size_in_bytes, "header is too big"
    header_bytes += b'\0' * \
        (padded_header_size_in_bytes - len(header_bytes))

    header_and_bundle = header_bytes + bundle

    snapshot_tensor = torch.frombuffer(
        bytearray(header_and_bundle), dtype=torch.uint8)
    # data is the real dictionary from jellyml.UserDict https://docs.python.org/3/library/collections.html#userdict-objects
    return {
        jellyml_dictionary_key: snapshot_tensor
    }


if __name__ == "__main__":

    snapshot = create_snapshot()
    a = {"fake_weights": torch.randn(
        (2, 2)), **snapshot}
    torch.save(a, "test_1.pt")  # type: ignore
    # b = {"fake_weights": torch.randn(
    #     (2, 2))} | snapshot
    # torch.save(b, "test_2.pt")  # type: ignore
