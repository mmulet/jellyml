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
from io import BufferedReader, BufferedWriter


def buffered_write(from_fd: BufferedReader, to_fd: BufferedWriter, buffer_size: int = 134_217_728):
    """
    Write data to a file_descriptor in chunks of size buffer_size
    """
    for chunk in iter(lambda: from_fd.read(buffer_size), b""):
        to_fd.write(chunk)
    to_fd.flush()
