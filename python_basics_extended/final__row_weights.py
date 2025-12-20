"""
O capitão divide as pessoas em pé em uma fila em dois times. A primeira pessoa vai para o time 1, a segunda para o time 2, a terceira para o time 1, e assim por diante.

Crie uma função row_weights que:

Receba uma lista de inteiros positivos (pesos das pessoas), onde:
O tamanho da lista é maior que 0.
Retorne uma lista com dois inteiros:
O peso total do time 1.
O peso total do time 2.
Exemplo:

row_weights([10]) # [10, 0]
row_weights([10, 85, 90]) # [100, 85]
row_weights([8, 5, 9, 3]) # [17, 8]
"""

def row_weights(row: list) -> list:
    line_one = []
    line_two = []
    for person in range(0, len(row), 2):
        line_one.append(row[person])
    if len(row) > 1:
        for person in range(1, len(row), 2):
            line_two.append(row[person])
    else:
        line_two.append(0)
    return [sum(line_one),sum(line_two)]

print(row_weights([10]))
print(row_weights([10, 85, 90]))