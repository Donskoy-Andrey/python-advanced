""""Issue01, Issue02"""

from keyword import iskeyword


class ColorizeMixin:
    """Mixin that change color"""
    def __repr__(self):
        return f'\033[1;{Advert.repr_color_code};40m{super().__repr__()}'


class JSONParser:
    """Parser of JSON objects"""
    def __init__(self, mapping: dict):
        for key, value in mapping.items():

            if iskeyword(key):
                key += "_"

            if isinstance(value, dict):
                value = JSONParser(value)

            setattr(self, key, value)


class BaseAdvert:
    """Base class for Advert"""

    def __init__(self, mapping: dict):
        self._price = 0

        parser = JSONParser(mapping)
        for attribute in dir(parser):
            if not attribute.startswith('__'):
                setattr(self, attribute, parser.__getattribute__(attribute))

        if not hasattr(self, 'title'):
            raise ValueError(
                'Instance should contain `title` attribute.'
            )

    def __repr__(self):
        if hasattr(self, 'title') and hasattr(self, 'price'):
            return f'{self.title} | {self.price} ₽'
        raise AttributeError(
            'Instance should contain both `title` '
            'and `price` attributes to do `repr`.'
        )


class Advert(BaseAdvert):
    """Advert class"""

    # Text color if add ColorizeMixin
    repr_color_code = 60

    @property
    def price(self):
        """Return place"""
        return self._price

    @price.setter
    def price(self, value: float | int):
        """
        Set price

        :param value: new value
        """
        if value >= 0:
            self._price = value
        else:
            raise ValueError('must be >= 0')


class AdvertWithMixin(Advert, ColorizeMixin, BaseAdvert):
    """The same class as Advert but with Mixin"""
