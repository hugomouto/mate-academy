"""
Travel Destinations

5xp

Imagine que estamos planejando uma viagem ao redor do mundo. Escolhemos vários lugares para visitar e os registramos em um tuple destination, tendo em mente que nossos planos não irão mudar.

Mas agora... queremos adicionar outro ótimo lugar à sua lista. Para isso, crie uma função travel_destinations() que:

Receba um tuple destinations com os lugares já escolhidos e uma string new_destination.
Retorne um novo tuple com os lugares originais e o novo lugar ao final.
Por exemplo:

travel_destinations(("Paris", "London", "Berlin"), "Kyiv") # ("Paris", "London", "Berlin", "Kyiv")
"""


def travel_destinations(destinations: tuple, new_destination: str) -> tuple:
    new_entry = (new_destination,)
    new_destinations = destinations + new_entry
    return new_destinations