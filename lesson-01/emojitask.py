class BasePokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'


class EmojiMixin:
    name: str
    poketype: str

    def __str__(self):
        types = {
            'grass': '🌿',
            'fire': '🔥',
            'water': '💧',
            'electric': '⚡',
        }
        return f'{self.name}/{types[self.poketype]}'


class Pokemon(BasePokemon):
    pass


class PokemonWithMixin(EmojiMixin, BasePokemon):
    pass
