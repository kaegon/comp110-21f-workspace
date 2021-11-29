"""Example of a Point class."""
from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a Point with its x, y components."""
        self.x = x
        self.y = y 

    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components by factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Pure method that does not mutate the Point."""
        return Point(self.x * factor, self.y * factor)

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        print("__add__ was called")
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __str__(self) -> str:
        """Produce a str representation of a Point for a human."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str: 
        """Produce a str representation of a Point for Python."""  
        return f"Point({self.x}, {self.y})"  
    def __getitem__(self, index: int) -> float:
        """Overload subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError

p0: Point = Point(1.0, 2.0)
p0.scale_by(2.0)
print(f"{p0.x}, {p0.y}")

p1: Point = p0.scale(2.0)
print(f"{p1.x}, {p1.y}")

a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(str(c))

print(a[0])