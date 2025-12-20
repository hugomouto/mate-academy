"""
Não precisamos mais armazenar informações sobre o país dos nossos usuários. Portanto, decidimos remover o campo country do banco de dados — em duas etapas.

Escreva uma função que:

Remova o campo country para todos os usuários cujo status seja active.
Não retorne nada.
Por exemplo:

users = [
  { "name": "Emma", "status": "active", "country": "Ukraine" },
  { "name": "Avram", "status": "disabled", "country": "Poland" },
]

remove_country(users)

# users == [
#   { "name": "Emma", "status": "active"},
#   { "name": "Avram", "status": "disabled", "country": "Poland" },
# ]
"""

def remove_country(users: list) -> None:
    for user in users:
        if user["status"] == "active":
            del user["country"]

