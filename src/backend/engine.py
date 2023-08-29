"""Provide the class that handles the backend of the application.

This module allows the application to run and process information

Examples:

    >>> directory = path.dirname(path.realpath("__file__"))
    >>> app = PowerConsumption(root_path=directory)
    >>> csv_handler = app.create_csv()

The module contains the following class:
- `PowerConsumption`: A class that represents the engine of the application

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

    def __post_int__(self):
        """Validation of permission for the application to work"""
        authorize_rapl()
        authorize_cwd(self.root_path)

    def get_path(self) -> str:
        """Returns the working directory path.

        Returns:
            str: File path with file name
        """
        file_extension = self.file_name + ".csv"
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

    def parse_csv(self) -> tuple[float, float]:
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
            return (sum_duration, sum_energy)
