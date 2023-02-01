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
from .get_header_and_bundle_from_model import get_header_and_bundle_from_model
from .CommandDict import CommandDict
from os import path, getcwd
from .SubParsersType import SubParsersType
from .add_help_printer import add_help_printer
from typing_extensions import TypeGuard
from .add_option import add_option, options_with_help
from .print_extract_bundle_help import print_extract_bundle_help
from .add_help_to_parser import add_help_to_parser
from .print_info import print_info
from .ShellCode import ShellCode
from rich.console import Group
from dataclasses import dataclass
from os.path import sep
from typing import Optional


class ExtractBundleArgs:
    model: Optional[str]
    output_path: Optional[str]


class ExtractBundleArgsWithModel(ExtractBundleArgs):
    model: str


@dataclass
class ExtractBundleArgs_dataclass(ExtractBundleArgsWithModel):
    model: str
    output_path: Optional[str]


def has_model(args: ExtractBundleArgs) -> TypeGuard[ExtractBundleArgsWithModel]:
    return args.model is not None


def parse_extract_bundle_args(subparsers: SubParsersType, out_command_dict: CommandDict):
    command_name = "extract-bundle"

    extract_parser = subparsers.add_parser(
        command_name, add_help=False, help="Extract the git bundle from jellyml.a jelly filled model file")
    options: options_with_help = []
    help_name = "extract_bundle_help"
    add_help_to_parser(help_name, extract_parser)

    add_option(options, extract_parser,   "model", nargs="?",
               help="Path to the model file to fill")
    add_option(options, extract_parser,  "-o", "--output_path", required=False, help=f"""
    The path to extract the bundle to. Defaults to the current directory{sep}${{model_name}}.bundle.
    If you specify a directory, the bundle will be extracted to ${{output_path}}{sep}${{model_name}}.bundle
    """)

    out_command_dict[command_name] = add_help_printer(extract_bundle)(
        help_name, print_extract_bundle_help(options))  # type: ignore


def get_bundle_path(args: ExtractBundleArgsWithModel):
    if args.output_path is None:
        return path.join(getcwd(), f"{path.basename(args.model)}.bundle")
    elif path.isdir(args.output_path):
        return path.join(args.output_path, f"{path.basename(args.model)}.bundle")
    else:
        return args.output_path


def extract_bundle(args: ExtractBundleArgs) -> int:
    if not has_model(args):
        print_info(Group("You must specify a model file to extract the code from.",
                         "Example:",
                         ShellCode("jelly eat my_model.pth")))
        return 1
    # let exceptions bubble up
    _, bundle = get_header_and_bundle_from_model(args.model)
    out_path = get_bundle_path(args)
    with open(out_path, "wb") as f:
        f.write(bundle)
    return 0
