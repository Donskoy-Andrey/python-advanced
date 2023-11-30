import pytest
from typing import Any
import json
from issues import Advert, AdvertWithMixin


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ('lesson_ad.title', 'python'),
        ('lesson_ad.price', 0),
        ('lesson_ad.location.address', 'город Москва, Лесная, 7'),
        ('lesson_ad.location.metro_stations', ['Белорусская']),
    ]
)
def test_multi_nesting(test_input: str, expected: Any):
    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ('dog_ad.title', 'Вельш-корги'),
        ('dog_ad.price', 1000),
        ('dog_ad.class_', 'dogs'),
    ]
)
def test_keywords(test_input: str, expected: Any):
    dog_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs"
    }"""
    dog = json.loads(dog_str)
    dog_ad = Advert(dog)
    assert eval(test_input) == expected


def test_price_value_error_in_creating_instance():
    lesson_str = '{"title": "python", "price": -1}'
    lesson = json.loads(lesson_str)
    with pytest.raises(ValueError) as exc_info:
        lesson_ad = Advert(lesson)
    assert exc_info.value.args[0] == 'must be >= 0'


def test_price_value_error_after_creating_instance():
    lesson_str = '{"title": "python", "price": 1}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    with pytest.raises(ValueError) as exc_info:
        lesson_ad.price = -3
    assert exc_info.value.args[0] == 'must be >= 0'


def test_price_equals_zero():
    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.price == 0


@pytest.mark.parametrize(
    'test_price,expected_price',
    [
        (0, 0), (1, 1), (1000, 1000),
        (101.1, 101.1), (123.5, 123.5), (7.2, 7.2)
    ]
)
def test_normal_price(
    test_price: float | int, expected_price: float | int
):
    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    lesson_ad.price = 5.3
    assert lesson_ad.price == 5.3


def test_repr():
    iphone_ad = Advert({'title': 'iPhone X', 'price': 100})
    assert repr(iphone_ad) == 'iPhone X | 100 ₽'


def test_repr_with_mixin():
    iphone_ad = AdvertWithMixin({'title': 'iPhone X', 'price': 100})
    assert (
        repr(iphone_ad) ==
        f'\033[1;{Advert.repr_color_code};40miPhone X | 100 ₽'
    )


def test_no_title_attribute():
    with pytest.raises(ValueError) as exc_info:
        _ = Advert({'tilte': 'iPhone X', 'price': 100})
    assert exc_info.value.args[0] == (
        'Instance should contain `title` attribute.'
    )
