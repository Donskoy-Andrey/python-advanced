import pytest
from emojitask import Pokemon, PokemonWithMixin


@pytest.mark.parametrize(
    'name,poketype,output',
    [
        ('pika', 'electric', 'pika/electric'),
        ('nopika', 'water', 'nopika/water'),
    ]
)
def test_pokemon(name: str, poketype: str, output: str):
    pokemon = Pokemon(name=name, poketype=poketype)
    assert str(pokemon) == output


@pytest.mark.parametrize(
    'name,poketype,output',
    [
        ('pika', 'electric', 'pika/⚡'),
        ('nopika', 'water', 'nopika/💧'),
    ]
)
def test_pokemon_with_mixin(name: str, poketype: str, output: str):
    pokemon = PokemonWithMixin(name=name, poketype=poketype)
    assert str(pokemon) == output
