import sys


def print_version():
    if sys.argv[1] != "--version" and sys.argv[1] != "-v":
        return
    print("1.0.0")
    exit(0)
