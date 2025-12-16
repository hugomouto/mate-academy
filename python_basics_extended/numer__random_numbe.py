"""
Crie uma função generate_random_list() que:

Receba três valores:
limite inferior do intervalo — min_value.
limite superior do intervalo — max_value.
comprimento da lista — length.
Retorne uma lista do length especificado com inteiros aleatórios de min_value a max_value, inclusive.
Por exemplo:

generate_random_list(1, 1, 1) == [1]
generate_random_list(1, 3, 5) == [2, 3, 1, 1, 3]
generate_random_list(-1, 1, 3) == [0, 1, 1]
"""

import random

def generate_random_list(min_value: int, max_value: int, length: int) -> list:
    random_list = []
    for number in range(length):
        random_list.append(random.randint(min_value,max_value))
    return random_list

print(generate_random_list(-1, 1, 3))