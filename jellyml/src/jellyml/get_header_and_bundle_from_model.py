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
from zipfile import ZipFile
from .constants import padded_header_size_in_bytes
from json import loads
from .JellyMLSnapshotHeader import JellyMLSnapshotHeaderV1
from os.path import split
from typing import Tuple

class UnsupportedVersion(Exception):
    pass


class CouldNotFindSnapshot(Exception):
    pass


def get_header_and_bundle_from_model(path_to_model: str) -> Tuple[JellyMLSnapshotHeaderV1, bytes]:
    with ZipFile(path_to_model, mode="r") as zipfile:
        # note: /data still works on windows
        possible_files = [file_info for file_info in zipfile.infolist(
        ) if split(file_info.filename)[0].endswith(f"/data")]
        for file_info in possible_files:
            with zipfile.open(file_info, "r") as f:
                maybe_header = f.read(padded_header_size_in_bytes)
                try:
                    maybe_header = maybe_header.replace(b"\x00", b"")
                    header: JellyMLSnapshotHeaderV1 = loads(maybe_header)
                    if header["magic_number"] != "jelly_ml_snapshot":
                        continue
                    if header["version"] != "january-7-2023":
                        raise UnsupportedVersion(
                            "Unsupported version. Try updating JellyML")
                    # read the rest of the file as the bundle
                    bundle = f.read()
                    return (header, bundle)
                except:
                    continue
    raise CouldNotFindSnapshot(
        "Could not find any snapshots in the model file")


if __name__ == "__main__":
    a = get_header_and_bundle_from_model("test_1.pt")
    print(a)
