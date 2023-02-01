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
from .CommandDict import CommandDict
from .get_header_and_bundle_from_model import get_header_and_bundle_from_model
from .Run import Run
from .generate_temporary_bundle_path import generate_temporary_bundle_path
from .get_current_branch_name import get_current_branch_name
from .working_tree_is_clean import working_tree_is_clean
from datetime import datetime
from .JellyHistoryItem import JellyHistoryItemV1, JellyHistoryItemV1_base_incomplete
from .get_jelly_history import get_jelly_history
from .push_jelly_history import push_jelly_history
from .is_git_repository import is_git_repository
from .JellyHistoryArgs import JellyHistoryArgs, add_history_args_to_parser
from .SubParsersType import SubParsersType
from .get_current_commit_hash import get_current_commit_hash
from .VerbosityArgs import VerbosityArgs, add_verbosity_args_to_parser
from .add_help_printer import add_help_printer
from .add_help_to_parser import add_help_to_parser
from .add_option import add_option, options_with_help
from .print_eat_help import print_eat_help
from typing_extensions import TypeGuard, Protocol
from uuid import uuid4
from dataclasses import dataclass
from .print_info import print_info
from .ShellCode import ShellCode
from rich.console import Group
from .constants import eat_command_name
from typing import Optional


class EatArgs(JellyHistoryArgs, VerbosityArgs, Protocol):
    model: Optional[str]
    quiet: bool
    code_dir: Optional[str]
    no_donut: bool


class EatArgsWithModel(EatArgs,  Protocol):
    model: str


@dataclass
class EatArgsWithModel_dataclass(EatArgsWithModel):
    model: str
    quiet: bool
    code_dir: Optional[str]
    no_donut: bool


def parse_eat_args(subparsers: SubParsersType, out_command_dict: CommandDict):
    aliases = [
        "load", "load-snapshot-from"]

    eat_parser = subparsers.add_parser(eat_command_name, aliases=aliases,
                                       add_help=False, help="Extract a snapshot of your code from jelly-filled model")
    help_name = "eat_help"
    add_help_to_parser(help_name, eat_parser)

    options: options_with_help = []
    add_option(options, eat_parser, "model",
               nargs="?",
               help="The model file to extract the code from")

    add_history_args_to_parser(options, eat_parser)
    add_verbosity_args_to_parser(options, eat_parser)
    handler = add_help_printer(eat)(
        help_name, print_eat_help(options))  # type: ignore
    for c in [eat_command_name] + aliases:
        out_command_dict[c] = handler


def checkout_bundle(args: EatArgsWithModel, bundle_path: str) -> JellyHistoryItemV1:
    run = Run(args.code_dir)
    current_date_string = f"{datetime.now().date()}-{uuid4()}"
    base_history_item: JellyHistoryItemV1_base_incomplete = {
        "version": "january-07-2023",
        "date": current_date_string,
        "going_to_model_snapshot": args.model,
    }

    if not is_git_repository(run):
        # since it's not a git repository we will clone the bundle into the code directory instead of
        # stashing stuff, fetching, and checking out
        run(f"git clone --quiet {bundle_path}")
        model_snapshot_commit_hash = get_current_commit_hash(run)
        history_item: JellyHistoryItemV1 = {
            **base_history_item,
            "model_snapshot_commit_hash": model_snapshot_commit_hash,
            "type": "clone",

        }
        return history_item

    def get_stash_message():
        if working_tree_is_clean(run):
            return None
        else:
            stash_message = f"jellyml_stash_at_{current_date_string}"
            run(
                f"git stash --include-untracked --quiet -m '{stash_message}'")
            return stash_message
    stash_message = get_stash_message()

    current_branch_name, _ = get_current_branch_name(
        run)

    run(f"git fetch --quiet {bundle_path}")

    run(f"git checkout --quiet FETCH_HEAD")
    model_snapshot_commit_hash = get_current_commit_hash(run)

    history_item: JellyHistoryItemV1 = {
        **base_history_item,
        "type": "pull",
        "model_snapshot_commit_hash": model_snapshot_commit_hash,
        "git_branch_name_or_commit_hash": current_branch_name,
        "git_stash_message": stash_message,
    }
    return history_item


def has_model(args: EatArgs) -> TypeGuard[EatArgsWithModel]:
    if args.model is None:
        print_info(Group("You must specify a model file to extract the code from.",
                         "Example:",
                         ShellCode("jelly eat my_model.pth")))
        exit(1)
    return True


def eat(args: EatArgs) -> int:
    if not has_model(args):
        return 1
    run = Run(args.code_dir)
    # let exceptions bubble up
    _, bundle = get_header_and_bundle_from_model(args.model)
    bundle_path = generate_temporary_bundle_path()
    with open(bundle_path, "wb") as f:
        f.write(bundle)

    history = get_jelly_history(run)
    history_item = checkout_bundle(args=args, bundle_path=bundle_path)
    push_jelly_history(run, history, history_item)
    if not args.quiet:
        print_info(
            Group("Successfully loaded the snapshot into your working tree.",
                  "If you want to go back to your previous state, you can run this command:",
                  ShellCode("jelly undo")))
    return 0


if __name__ == "__main__":
    from .test_project_root_directory import project_root_directory
    from os.path import join
    eat(EatArgsWithModel_dataclass(
        model=join(project_root_directory, "tensor.pt"),
        quiet=True,
        code_dir=join(project_root_directory, "test_git_repo"),
        no_donut=False
    ))
