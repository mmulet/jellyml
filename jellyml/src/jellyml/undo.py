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
from .JellyHistoryArgs import JellyHistoryArgs, add_history_args_to_parser
from .SubParsersType import SubParsersType
from .CommandDict import CommandDict
from .get_jelly_history import get_jelly_history
from .Run import Run
from .pop_jelly_history import pop_jelly_history
from .VerbosityArgs import VerbosityArgs, add_verbosity_args_to_parser
from .add_option import options_with_help
from .add_help_to_parser import add_help_to_parser
from .add_help_printer import add_help_printer
from .print_undo_help import print_undo_help
from .find_entry_in_stash import find_entry_in_stash
from .print_info import print_info
from rich.console import Group
from dataclasses import dataclass
from .constants import undo_command_name
from .create_new_branch_for_changes_after_eating import create_new_branch_for_changes_after_eating
from typing import Optional

class UndoArgs(JellyHistoryArgs, VerbosityArgs):
    quiet: bool
    code_dir: Optional[str]
    no_donut: bool


@dataclass
class UndoArgs_dataclass(UndoArgs):
    quiet: bool
    code_dir: Optional[str]
    no_donut: bool


def parse_undo_args(subparsers: SubParsersType, out_command_dict: CommandDict):
    aliases = ["undonut", "return"]
    help_name = "undo_help"
    undo_parser = subparsers.add_parser(undo_command_name, aliases=aliases, add_help=False, help="""
        Undo the last jellyml command.
    """)
    options: options_with_help = []
    add_help_to_parser(help_name, undo_parser)

    add_history_args_to_parser(options, undo_parser)
    add_verbosity_args_to_parser(options, undo_parser)

    handler = add_help_printer(undo)(
        help_name, print_undo_help(options))  # type: ignore
    for c in [undo_command_name] + aliases:
        out_command_dict[c] = handler


def undo(args: UndoArgs) -> int:
    run = Run(git_repo_path=args.code_dir)

    history = get_jelly_history(run)
    if len(history["history_stack"]) <= 0:
        print_info(Group("There is nothing to undo."))
        return 0
    last_item = history["history_stack"][-1]
    if last_item["type"] == "clone":
        print_info(
            Group("The last thing you did was clone a snapshot. Can't undo a clone."))
        return 0
    if last_item["type"] != "pull":
        # THis should never happen because of the checks in get_jelly_history
        print_info(
            Group(f"""Unrecognized history item type: { { last_item['type']}}.
This could be from an outdated version of jellyml. You may have to update jellyml."""))
        return -1
    run = Run(git_repo_path=args.code_dir)

    # let's check that the HEAD is pointing to the commit we expect it to
    # if it isn't, then we can't undo

    create_new_branch_for_changes_after_eating(
        run,
        last_item=last_item,
        quiet=args.quiet,
    )

    run(
        f"git checkout --quiet {last_item['git_branch_name_or_commit_hash']}")
    if last_item["git_stash_message"] is not None:
        stash_entry = find_entry_in_stash(run,
                                          message=last_item["git_stash_message"])
        if stash_entry is None:
            raise Exception(
                f""""Undo failed.
Reason: Could not find stash entry with message {last_item['git_stash_message']}
Why did this happen: When you used jellyml load-from-snapshot, you had uncommitted changes in your working tree.
(Ie modified or added files to your working tree that you had not yet committed.).
We stashed those changes using the git stash command.
When you used jellyml undo, we tried to pop those changes back into your working tree.
But we couldn't find the stash entry that we created when you used jellyml load-from-snapshot.
Usually this means that you have used git stash pop in the meantime, which means that the stash entry we created is no longer there.
It is very hard to lose information when using git, so those changes are likely to be still there somewhere. Probably in a commit.
You can use `git reflog` or `git log` to find the commit that contains the changes that you lost.""")

        run(
            f"git stash pop --quiet {stash_entry}")

    pop_jelly_history(run, jelly_history=history)
    return 0
