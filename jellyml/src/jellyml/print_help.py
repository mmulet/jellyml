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
from rich.panel import Panel
from rich.console import group
from rich.text import Text
from rich.table import Table
from .ShellCode import ShellCode
from .print_info import print_info
from rich.syntax import Syntax


def python_example():
    return Syntax("""import jellyml
import torch

# At the start of your training script
# create a snapshot of your code
snapshot = jellyml.create_jelly_filling()
# or use its alias "create_snapshot"
# if you are not in a whimsical mood
snapshot = jellyml.create_snapshot()
# your code here, like actually
# train your model...
...
# then, add one extra line when
# you save your model
torch.save({
    "model_state_dict": 
            model.state_dict(),
    # this will add the
    # snapshot to the model file
    **snapshot,
}, "my_model.pth")
""", "python", line_numbers=False)


@group()
def text_group():
    yield Panel.fit(Text("usage: jellyml (or jelly or jly) {eat,undo,git,fix} ...\n"))

    yield """A tool/library for embedding a snapshot of your code into a pytorch model file.
The code is the jelly filling to your model's donut.
Here's how you would typically use it:

1. Make sure git is installed. Get it here:
[blue underline]git-scm.com/downloads[/blue underline]
(some terminals may not follow links)

1.5 (optional) If this help doesn't look perfect,  download a terminal with rich text support. See: [blue underline]jellyml.com/docs.html[/blue underline]

2. Create a model file with the snapshot of your code embedded in it
"""
    yield Panel.fit(python_example(),
                    title="python",
                    border_style="yellow")
    yield """3. Later on, when you want to load the exact code that was used to create the model,
you can load the code from the model file with the command :"""
    yield ShellCode("jellyml load-snapshot-from my_model.pth")
    yield "or"
    yield ShellCode("jellyml eat my_model.pth")
    yield "(It's called \"eat\" because you are consuming the jelly filling from the donut.)"


    yield """\nHere are all the commands you can use with jellyml:"""
    table = Table(expand=True, padding=(0, 1), show_lines=True)
    table.add_column("command", justify="right", no_wrap=True)
    table.add_column("description")
    table.add_row(
        "eat\nload\nload-snapshot-from", "Extract a snapshot of your code from a jelly-filled model")
    table.add_row("undonut\nundo\nreturn",  "Undo the last jellyml command.")
    table.add_row(
        "git", "Advanced. Forward the rest of the arguments to git, using the model file as the git repo.")
    table.add_row("fix",
                  "Advanced. A collection of subcommands for fixing common problems. Use jly fix -h for more info.")
    yield table
    yield Text("Examples:")
    yield ShellCode("jellyml eat my_model.pth")
    yield ShellCode("jelly undo")
    yield ShellCode("jly fix extract-bundle my_model.pth")
    yield "Use -h on each command for more info."
    yield "for example:"
    yield ShellCode("jellyml eat -h")

    yield """\nLast, but not least, I've added a secret way to use the jellyml cli.
There is a clue in each command's help message, see if you can find it.
You can go to [blue underline]github.com/mmulet/jellyml/secret_hint.md[/blue underline]  for a hint.
(some terminals may not follow links)
While you are there, you could also star the repo."""


def print_help():
    print_info(text_group())


if __name__ == "__main__":
    print_help()
    # from rich.console import Console
    # console = Console(record=True)
    # console.print(python_example())
    # console.save_html("python_example.html")
