"""
Упакуйте только что написанный код в декторатор.
Весь вывод фукнции должен быть помечен временными метками так, как видно выше.
"""

import datetime
import sys
from typing import Callable
from functools import wraps, partial


def my_write(string_text: str, original_write: Callable) -> int:
    """
    New write function with execution time.

    :param original_write: original write function
    :param string_text: some text.
    :return:
        string's byte size.
    """
    timestamp = (
        datetime.datetime.now()
        .strftime("[%Y-%m-%d %H:%M:%S]")
    )
    if string_text != '\n':
        return original_write(f'{timestamp}: {string_text}')
    return original_write('')


def timed_output(function: Callable) -> Callable:
    """
    Decorator that add execution time to func

    :param function: function to change
    :return:
        Modified function
    """

    @wraps(function)
    def wrapper(*args, **kwargs):
        original_write = sys.stdout.write

        sys.stdout.write = partial(my_write, original_write=original_write)
        function(*args, **kwargs)
        sys.stdout.write = original_write

    return wrapper


@timed_output
def print_greeting_with_deco(name: str):
    """
    Greeting person with log-print

    :param name: person's name
    """
    print(f'Hello, {name}!')


def print_greeting_no_deco(name: str):
    """
    Greeting person with ordinary print

    :param name: person's name
    """
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting_no_deco('Nikita')
    print_greeting_with_deco('Nikita')
