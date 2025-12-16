"""
Crie uma função create_list que:

Receba um inteiro n.
Retorne uma lista com todos os inteiros pares de 1 a n, inclusive, e, se n = 0, retorne uma lista vazia.
Recomendamos usar:

Loop forpara iterar de 1a n.
Declaração if para verificar se o número é par.
Função range para gerar números.
Método append para adicionar números à lista.
Palavra-chave return para retornar a lista.
"""


def create_list(n):
    # Cria uma lista com os números de 1 até n
    n_list = list(range(n+1))
    # Nova lista que vai receber os números pares "even_numbers"
    even_numbers = []
    if n == 0:
        return even_numbers
    # For Loop pra passar de nḿero em número
    for number in n_list:
        # If para verificar se é par. Se for par, fazer append em "even_numbers"
        if number % 2 == 0:
            even_numbers.append(number)
    # Retorna "even_nmbers"
    return even_numbers

print(create_list(0))