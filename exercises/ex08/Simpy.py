"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730401999"


class Simpy:
    """An simulation of a common library NumbPy."""
    values: list[float]

    def __init__(self, values: list[float]): 
        """Initialize a new Simpy object."""
        self.values = values

    def __str__(self) -> str:
        """Str representation of a Simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, times: int) -> None:
        """Fill values array by mutating object."""
        self.values = []
        i: int = 0
        while i < times:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Gives a list of floats from one value to another in a defined step."""
        # Start an empty values list:
        self.values = []
        # Be sure step is not 0.0 by asserting
        assert step != 0.0 
        # When step is positive:
        if step > 0.0:
            # Initialize next value to start
            next_value: float = start
            # While next value is less than stop value
            while next_value < stop:
                # Add next value to values list
                self.values.append(next_value)
                # Update next value to by
                next_value += step
        if step < 0.0:
            # Initialize next value to start
            next_value: float = start
            # While next value is less than stop value
            while next_value > stop:
                # Add next value to values list
                self.values.append(next_value)
                # Update next value to by
                next_value += step

    def sum(self) -> float:
        """Delagate this algo to the built-in sum function."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloading the addition operator for simpy and/or float objects."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for x in self.values:
                result.values.append(x + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1      
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloading the power operator for simpy and/or float objects."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for x in self.values:
                result.values.append(x ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1      
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloading the == operator for simpy and simpy/float."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for x in self.values:
                result.append(x == rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloading the == operator for simpy and simpy/float."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for x in self.values:
                result.append(x > rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Giving the Simpy type subscription notation ability."""
        if isinstance(rhs, int):
            result_one: float = self.values[rhs]
            return result_one
        else:
            assert len(self.values) == len(rhs)
            result_two: Simpy = Simpy([])
            i: int = 0
            while i < len(self.values):
                if rhs[i]:
                    result_two.values.append(self.values[i])
                i += 1
            return result_two