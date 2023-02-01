from subprocess import run
from os import getcwd
from typing import Optional

class Run:
    def __init__(self, git_repo_path: Optional[str]) -> None:
        self.git_repo_path = git_repo_path

    def __call__(self, command: str):  # type: ignore
        return self.run(command)  # type: ignore

    def run(self, command: str):  # type: ignore
        return run(command, shell=True, cwd=self.git_repo_path,
                   check=True)  # type: ignore

    def get(self, command: str) -> str:  # type: ignore
        return run(command, shell=True, cwd=self.git_repo_path,
                   check=True, capture_output=True).stdout.decode('utf-8').strip()  # type: ignore

    def get_working_directory_path(self):
        return getcwd() if self.git_repo_path is None else self.git_repo_path

    def get_repo_path_args(self):
        return "" if self.git_repo_path is None else f"git_repo_path={ self.git_repo_path},"
