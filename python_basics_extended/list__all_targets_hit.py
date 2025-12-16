"""
Em uma recente competição de arco e flecha, os jurados gastaram muito tempo verificando se cada atleta acertou todos os alvos pelo menos uma vez. Vamos automatizar essa verificação.

Crie uma função all_targets_hit() que:

Receba uma lista attempts_for_each_target, onde cada sublista contém valores booleanos — resultados dos disparos:
True para acerto.
False para erro.
Retorne True se todos os alvos foram acertados pelo menos uma vez; caso contrário, retorne False.
Por exemplo:

attempts = [
  [True, False, True],        # Shots at the first target
  [False, True, False, True], # Shots at the second target
  [False, True],              # Shots at the third target
]
all_targets_hit(attempts) # True, all targets were hit at least once

attempts = [
  [True, False, True],        # Shots at the first target
  [False, False, True],       # Shots at the second target
  [False, False],             # Shots at the third target
]
all_targets_hit(attempts) # False, the third target was not hit
"""

def all_targets_hit(attempts_for_each_target: list) -> bool:
    result = []
    for list in attempts_for_each_target:
        if any(list):
            result.append(True)
        else:
            result.append(False)
    return all(result)