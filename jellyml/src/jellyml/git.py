#pyright: reportPrivateUsage=false
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
from subprocess import run
from .CommandDict import CommandDict
from .generate_temporary_bundle_path import generate_temporary_bundle_path
from .get_header_and_bundle_from_model import get_header_and_bundle_from_model
from argparse import REMAINDER
from .SubParsersType import SubParsersType
from .add_help_to_parser import add_help_to_parser
from .add_help_printer import add_help_printer
from .print_git_help import print_git_help
from dataclasses import dataclass
from typing_extensions import Protocol
from .constants import git_command_name
from typing import List

class GitArgs(Protocol):
    args: List[str]


@dataclass
class GitArgs_dataclass(GitArgs):
    """
    The first arg, args[0], Should be 
    the path to the model file.
    Example:
    ```python
    args = ["model_file.pt", "fetch", "{}"]
    ```
    """
    args: List[str]


def parse_git_args(subparsers: SubParsersType, out_command_dict: CommandDict):
    help_name = "git_help"
    git_parser = subparsers.add_parser(git_command_name,   help="""
    Forward the rest of the arguments to git,
    using the model file as the git repo.
    Use `jelly git -h` for more info.
    """, add_help=False,
                                       usage="""
    jelly git path_to_model_file [git_args]
    {} will be replaced as the path to the git repo
    Example:
    Change
    git clone https://jellyml.com/my_repo.git
    to
    jelly git model_file.pt clone {}
    More examples:
    jelly git model_file.pt fetch {}
    jelly git model_file.pt checkout {}
    """,
                                       )
    add_help_to_parser(help_name, git_parser)

    # git_parser.add_argument("model", help="Path to the model file")
    git_parser.add_argument("args", nargs=REMAINDER)
    out_command_dict[git_command_name] = add_help_printer(
        git)(help_name, print_git_help)  # type: ignore


def git(args: GitArgs):
    model_path = args.args[0]
    git_args = args.args[1:]
    # let exceptions bubble up
    _, bundle = get_header_and_bundle_from_model(model_path)
    bundle_path = generate_temporary_bundle_path()
    with open(bundle_path, "wb") as f:
        f.write(bundle)
    replaced_args = [
        arg if arg != "{}" else bundle_path for arg in git_args]
    run(["git"] + replaced_args, check=True)
    return 0
