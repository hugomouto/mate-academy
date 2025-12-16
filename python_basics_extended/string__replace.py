"""
Estamos organizando um evento e o local foi alterado de última hora. Precisamos atualizar o anúncio rapidamente substituindo o local antigo.

Crie uma função update_announcement() que:

Receba uma string original_announcement, a palavra a ser substituída (old_place) e a palavra que a substituirá (new_place).
Use o método replace para substituir old_place por new_place em original_announcement.
Retorne o anúncio atualizado.
Por exemplo:

update_announcement("The meeting will take place in the park.", "park", "cafe") # "The meeting will take place in the cafe."
update_announcement("Don't forget to bring umbrellas, it will rain!", "rain", "sun") # "Don't forget to bring umbrellas, it will sun!"
"""

def update_announcement(original_announcement: str, old_place: str, new_place: str) -> str:
   return original_announcement.replace(old_place,new_place)
