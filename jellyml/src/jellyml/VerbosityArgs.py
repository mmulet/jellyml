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
from typing_extensions import Protocol, Any
from argparse import ArgumentParser
from .DonutLogo import disable_donut_logo
from .add_option import add_option, options_with_help


class VerbosityArgs(Protocol):
    quiet: bool
    no_donut: bool


def add_verbosity_args_to_parser(options: options_with_help, parser: ArgumentParser):
    add_option(options, parser, "-q", "--quiet",
               action="store_true", help="If set, the program won't print any info messages to the console. It will only print warnings and errors.")
    add_option(options, parser, "--no_donut",
               action="store_true", help="Suppress the donut logo")


def handle_logo(args: Any):
    if getattr(args, "no_donut", False):
        disable_donut_logo()
