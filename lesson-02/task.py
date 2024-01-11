"""Все самое важное в классах 2: практика"""
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Constants:
    """Class with all constants"""

    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'


class ComputerColor(ABC):
    """Protocol for Color class"""

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, other: float):
        pass

    @abstractmethod
    def __rmul__(self, other: float):
        pass


class Color(ComputerColor):
    """Class that return colored dot"""

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return (
            f'{Constants.START};{self.red};'
            f'{self.green};{self.blue}{Constants.MOD}'
            f'⚫{Constants.END}{Constants.MOD}'
        )

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other: "Color") -> bool:
        if not isinstance(other, Color):
            return NotImplemented

        return (
            (self.red, self.green, self.blue) ==
            (other.red, other.green, other.blue)
        )

    def __add__(self, other: "Color") -> "Color":
        if not isinstance(other, Color):
            return NotImplemented

        return Color(
            min(self.red + other.red, 255),
            min(self.green + other.green, 255),
            min(self.blue + other.blue, 255)
        )

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __mul__(self, other: float):
        if not 0 <= other <= 1:
            raise ValueError(
                'Contrast coefficient should be from [0, 1]'
            )

        cl = -256 * (1 - other)
        F = 259 * (cl + 255) / (255 * (259 - cl))

        def new_color(color: int):
            return int(F * (color - 128) + 128)

        return Color(
            min(new_color(self.red), 255),
            min(new_color(self.green), 255),
            min(new_color(self.blue), 255),
        )

    def __rmul__(self, other: float):
        return self.__mul__(other)


def print_a(color: ComputerColor):
    """
    Beautiful print for letter `A`

    :param color: instance with colored dot
    """
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] +
        [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 +
        [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 +
        [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 +
        [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))
