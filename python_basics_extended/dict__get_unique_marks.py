"""
Na turma 4-A, muitos pais estão reclamando que um dos professores só dá notas 2 ou 12. Para verificar se isso é verdade, precisamos descobrir quais notas únicas ele deu recentemente.

Crie uma função get_unique_marks que:

Receba o registro escolar class_register. É um dicionário, onde:
As chaves são os nomes dos alunos.
Os valores são as notas que eles receberam.
Retorne uma lista de notas únicas.
Por exemplo, para este registro:

class_register = {
  "Robb Stark": 2,
  "Sansa Stark": 12,
  "Arya Stark": 2,
  "Bran Stark": 2,
  "Jon Snow": 2,
}

...get_unique_marks deve retornar uma lista [2, 12].
"""

def get_unique_marks(class_register: dict) -> list:
    class_register_values = list(class_register.values())
    return list(set(class_register_values))

"""
class_register = {
  "Robb Stark": 2,
  "Sansa Stark": 12,
  "Arya Stark": 2,
  "Bran Stark": 2,
  "Jon Snow": 2,
}
class_register_values = list(class_register.values())

print(list(set(class_register_values)))

"""