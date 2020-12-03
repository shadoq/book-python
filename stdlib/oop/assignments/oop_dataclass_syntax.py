"""
* Assignment: OOP Dataclass Syntax
* Filename: oop_dataclass_syntax.py
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use Dataclass to define class `Point`
    2. Class has attributes:
        a. `x: int` with default value `0`
        b. `y: int` with default value `0`
    3. When `x` or `y` has negative value raise en exception `ValueError('Coordinate cannot be negative')`
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj Dataclass do zdefiniowania klasy `Point`
    2. Klasa ma atrybuty:
        a. `x: int` z domyślną wartością `0`
        b. `y: int` z domyślną wartością `0`
    3. Gdy `x` lub `y` mają wartość ujemną podnieś wyjątek `ValueError('Coordinate cannot be negative')`
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isclass
    >>> assert isclass(Point)
    >>> assert hasattr(Point, 'x')
    >>> assert hasattr(Point, 'y')

    >>> Point()
    Point(x=0, y=0)

    >>> Point(x=0, y=0)
    Point(x=0, y=0)

    >>> Point(x=1, y=2)
    Point(x=1, y=2)

    >>> Point(x=-1, y=0)
    Traceback (most recent call last):
    ValueError: Coordinate cannot be negative

    >>> Point(x=0, y=-1)
    Traceback (most recent call last):
    ValueError: Coordinate cannot be negative
"""


# Given
from dataclasses import dataclass


# Solution
@dataclass
class Point:
    x: int = 0
    y: int = 0

    def __post_init__(self):
        if self.x < 0 or self.y < 0:
            raise ValueError('Coordinate cannot be negative')