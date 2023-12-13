"""
Для начала, давайте подменим метод write у объекта sys.stdin на такую функцию,
которая перед каждым вызовом оригинальной функции записи данных
в stdout допечатывает к тексту текущую метку времени.
"""

import sys
import datetime


original_write = sys.stdout.write


def my_write(string_text: str) -> int:
    """
    New write function with execution time.

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


if __name__ == '__main__':
    sys.stdout.write = original_write
    print('1, 2, 3')

    sys.stdout.write = my_write
    print('1, 2, 3')
