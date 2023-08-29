"""Provide the functions to change authorizations for the application to run.

This module changes permissions intel RAPL and local directories.

Examples:

    >>> authorize_rapl()
    >>> authorize_cwd(path_chosen)

The module contains the following functions:
- `authorize_rapl`: A function tht changes the permissions of the Intel RAPL
    directory.
- `authorize_cwd`: A function tht changes the permissions of the chosen
    directory.
"""

import subprocess


def authorize_rapl():
    """Changes the permissions of the Intel RAPL directory"""
    print("Change permissions to run Intel RAPLs")
    subprocess.run(
        "sudo chmod -R a+r /sys/class/powercap/intel-rapl",
        shell=True,
        stdout=subprocess.PIPE,
        check=True,
    )


def authorize_cwd(path: str):
    """Changes the permissions of the chosen directory

    Args:
        path (str): Chosen directory
    """
    print("Change permissions of current directory")
    command = f"sudo chmod -R 777 {path}"
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, check=True)
