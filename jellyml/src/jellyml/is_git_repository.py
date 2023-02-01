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
from .Run import Run


def is_git_repository(run: Run):
    try:
        # git rev-parse --is-inside-work-tree returns true if the current directory is a git repo
        # and an error if it is not, the error will be passed to the except block by check=True
        run.get(f"git rev-parse --is-inside-work-tree")
        return True
    except:
        return False
