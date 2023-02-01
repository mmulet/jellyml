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
from typing_extensions import Protocol
from argparse import ArgumentParser
from .add_option import add_option, options_with_help
from os.path import sep
from typing import Optional

class JellyHistoryArgs(Protocol):
    code_dir: Optional[str]


def add_history_args_to_parser(options: options_with_help, parser: ArgumentParser):
    add_option(options, parser, "-c", "--code_dir",
               help=f"""The directory of the git repo to fill the model with.
Defaults to the current working directory.

Can be inside a folder of a git repo. For example, if your git repo is at
user{sep}repo, you can use
user{sep}repo{sep}src as the code_dir.""")
