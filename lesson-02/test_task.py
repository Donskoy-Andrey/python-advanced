import pytest
from unittest.mock import patch, call
from task import Color, Constants, print_a
import random


@pytest.mark.parametrize(
    "red,green,blue",
    [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
    ]
)
def test_red_dot(red: int, green: int, blue: int):
    dot = Color(red, green, blue)
    assert (
        str(dot) ==
        f'{Constants.START};{red};{green};{blue}{Constants.MOD}'
        f'⚫{Constants.END}{Constants.MOD}'
    )


@pytest.mark.parametrize(
    "red,green,blue",
    [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
    ]
)
def test_eq_method(red: int, green: int, blue: int):
    dot_1 = Color(red, green, blue)
    dot_2 = Color(red, green, blue)
    assert dot_1 == dot_2


@pytest.mark.parametrize(
    "red,green,blue",
    [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
    ]
)
def test_not_eq_method(red: int, green: int, blue: int):
    dot_1 = Color(red, green, blue)
    dot_2 = Color(red + 1, green + 1, blue + 1)
    assert dot_1 != dot_2


def test_return_not_implemented():
    dot_1 = Color(0, 0, 0)
    dot_2 = 12345
    assert dot_1 != dot_2


def test_add_with_colored_dots():
    dot_1 = Color(255, 0, 0)
    dot_2 = Color(0, 255, 0)
    dot_3 = Color(0, 0, 255)

    new_dot = dot_1 + dot_2 + dot_3

    assert (
        str(new_dot) ==
        f'{Constants.START};255;255;255{Constants.MOD}'
        f'⚫{Constants.END}{Constants.MOD}'
    )


def test_set_with_colored_dots():
    dot_1 = Color(255, 0, 0)
    dot_2 = Color(0, 255, 0)
    dot_3 = Color(0, 0, 255)

    assert {dot_1, dot_2, dot_3, dot_2, dot_2}.difference(
        {dot_1, dot_2, dot_3}
    ) == set()


@pytest.mark.parametrize(
    'other',
    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
)
def test_change_contrast(other: float):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    dot = Color(red, green, blue)
    new_dot = dot * other
    cl = -256 * (1 - other)
    F = 259 * (cl + 255) / (255 * (259 - cl))
    new_red = int(F * (red - 128) + 128)
    new_green = int(F * (green - 128) + 128)
    new_blue = int(F * (blue - 128) + 128)

    assert (
        str(new_dot) ==
        f'{Constants.START};{new_red};{new_green};{new_blue}'
        f'{Constants.MOD}⚫{Constants.END}{Constants.MOD}'
    )


def test_change_contrast_error():
    dot = Color(100, 100, 100)
    with pytest.raises(ValueError) as exc_info:
        _ = dot * 1.2
    assert (
        exc_info.value.args[0] ==
        'Contrast coefficient should be from [0, 1]'
    )


@pytest.mark.parametrize(
    "red,green,blue",
    [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
    ]
)
def test_print_a(red: int, green: int, blue: int):
    dot = Color(255, 0, 0)
    with patch('task.print') as mock_print:
        print_a(dot)

    color = dot
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

    result = []
    for row in a_matrix:
        result.append(call(''.join(str(ptr) for ptr in row)))

    assert mock_print.mock_calls == result
