"""Provide the class and functions that handles the backend of
the application.

This module allows the application to run and process information

Examples:

    >>> directory = path.dirname(path.realpath("__file__"))
    >>> app = PowerConsumption(root_path=directory)
    >>> csv_handler = app.create_csv()

The module contains the following class:
- `PowerConsumption`: A class that represents the engine of the application.

The module contains the following functions:
- `print_welcome_message`: Prints welcome message.
- `set_file_name`: User input for the output file name.
- `render_result`: Render the results.

"""
from dataclasses import dataclass
from os import path as pt
from typing import Any, Callable, TypeAlias

from pyJoules.handler.csv_handler import CSVHandler

from .bash import authorize_cwd, authorize_rapl

FunctionHandler: TypeAlias = Callable[[Any], None]


@dataclass(frozen=True)
class PowerConsumption:
    """A class used to represent the game engine.

    Attributes:
        root_path: str
            It is absolute path of the working directory.
        file_name: str = "result"
            It is the name of the file where the data is going to be saved.
            Default to 'result'.

    Methods:
        create_csv(self) -> CSVHandler:
            Returns the handler where the data is going to be save.
        get_path(self) -> str:
            Returns the working directory path.
        parse_csv(self) -> None:
            Parse the information save and return the total of energy
            consume.
    """

    root_path: str
    file_name: str = "result"

    def start(self):
        """Validation of permission for the application to work"""
        print_welcome_message()
        authorize_rapl()
        authorize_cwd(self.root_path)

    def get_path(self) -> str:
        """Returns the working directory path.

        Returns:
            str: File path with file name
        """
        name = set_file_name(self.file_name)
        file_extension = name + ".csv"
        abs_file_path = pt.join(self.root_path, file_extension)
        return abs_file_path

    def create_csv(self) -> CSVHandler:
        """Returns the handler where the data is going to be save.

        Returns:
            CSVHandler: Handler of the file where the information is going
                to be save
        """
        file_path = self.get_path()
        csv_file = CSVHandler(file_path)
        return csv_file

    def parse_csv(self) -> None:
        """Parse the information save and return the total of energy
        consume.
        """
        file_extension = self.file_name + ".csv"
        abs_file_path = pt.join(self.root_path, file_extension)
        with open(abs_file_path) as csv_file:
            next(csv_file)
            sum_duration = 0
            sum_energy = 0
            for line in csv_file:
                columns = line.split(";")
                sum_duration += float(columns[2])
                sum_energy += float(columns[3])
            render_result(sum_energy, sum_duration)


def print_welcome_message():
    """Prints welcome message"""
    print("Welcome to the Power App")
    print("For now it just runs on Linux")
    print("Get ready to now how much energy you script consumes")


def set_file_name(default: str) -> str:
    """User input for the output file name

    Returns:
        str: Returns file name selected or 'result'
    """
    print("What name of the output file")
    file_name: str = input("Enter for default('result'): ").strip()
    if file_name == "":
        return default
    return file_name


def render_result(sum_energy: float, sum_duration: float) -> None:
    """Render the results"""
    joules = sum_energy / 1000000
    print(f"Total energy {joules} J")
    print(f"Total energy {sum_duration} s")
    watt = joules / sum_duration
    print(f"Total power {watt} W")
