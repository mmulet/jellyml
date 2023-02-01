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
import argparse
from .eat import parse_eat_args
from .git import parse_git_args
from .undo import parse_undo_args
from .CommandDispatcher import CommandDispatcher
from .print_help import print_help
from .print_fix_help import print_fix_help
from .fix import parse_fix_args
from rich.traceback import install
from .VerbosityArgs import handle_logo
from .check_if_git_is_available import check_if_git_is_available
from .secret import process_secret_args
from .print_money_box import register_money_box_atexit
from .add_code import parse_add_code_args
from .puzzle_answer import parse_puzzle_args
from .print_version import print_version
install(show_locals=False)

def main():
    register_money_box_atexit()
    try:
        print_version()

        check_if_git_is_available()

        secret_args = process_secret_args()

        parser = argparse.ArgumentParser(
            prog="jellyml",
            add_help=False,
            description="A tool/library for embedding a snapshot of your code into a pytorch model file")
        command_dispatcher = CommandDispatcher(parser, "command", [

            parse_eat_args, parse_undo_args,
            parse_git_args,
            parse_fix_args,
            parse_add_code_args,
            parse_puzzle_args
        ])
        parser.add_argument("-h", "--help", action="store_true",
                            help="show this help message and exit")

        args = parser.parse_args(
            secret_args if secret_args is not None else None)
        if getattr(args, "fix_help", False):
            print_fix_help()
            exit(0)
        if args.help:
            print_help()
            exit(0)

        handle_logo(args=args)

        result = command_dispatcher.dispatch(args)
        if result != -12043:
            return result
        print_help()
    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
