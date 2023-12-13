"""
Напишите декторатор, который будет перенаправлять вывод фукнции в файл.
Подсказка: вы можете заменить объект sys.stdout каким-нибудь другим объектом.
"""

import sys
from typing import Callable
from functools import wraps


def redirect_output(filepath: str) -> Callable:
    """
    Parametrize decorator with output filename
    :param filepath: filepath
    :return:
        Parametrized decorator
    """
    def decorator(function: Callable) -> Callable:
        """
        Redirect output to file
        :param function: callable function
        :return:
            Modified function
        """
        @wraps(function)
        def wrapper(*args, **kwargs):
            original_out = sys.stdout

            with open(filepath, 'w', encoding='utf-8') as file:
                sys.stdout = file
                function(*args, **kwargs)

            sys.stdout = original_out
        return wrapper
    return decorator


@redirect_output('./function_output.txt')
def calculate():
    """Calculate powers"""

    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    calculate()
