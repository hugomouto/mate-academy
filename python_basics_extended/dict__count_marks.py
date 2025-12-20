"""
Na turma 5-A, muitos pais estão reclamando que não conseguem lidar com a tarefa de cálculo diferencial dada às crianças para o teste. Precisamos verificar se a tarefa é muito difícil para os alunos do quinto ano reunindo estatísticas sobre as notas recebidas.

Crie uma função count_marks que:

Receba um dicionário class_register, onde as chaves são os nomes dos alunos e os valores são suas notas.
Retorne um dicionário no mesmo formato.
Por exemplo, dado este dicionário:

class_register = {
  "Robb Stark": 10,
  "Sansa Stark": 12,
  "Arya Stark": 6,
  "Bran Stark": 8,
  "Jon Snow": 8,
}

...a função deve retornar:

count_marks(class_register) == {
  6: 1,
  8: 2,
  10: 1,
  12: 1,
}
"""

def count_marks(class_register: dict) -> dict:
    value_list = list(class_register.values())
    value_list.sort()
    marks_list = {}
    for item in value_list:
        marks_list.update({item: value_list.count(item)})
    return marks_list 