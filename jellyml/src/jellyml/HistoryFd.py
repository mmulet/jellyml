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
from .Run import Run


class HistoryFd:
    def __init__(self, run: Run, mode: str):
        path = get_jelly_history_path(run)
        self.fd = open(path, mode)

    def __enter__(self):
        return self.fd

    def __exit__(self, exc_type, exc_value, traceback):  # type: ignore
        self.fd.close()
