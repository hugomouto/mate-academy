"""
Programadores adoram nomes de variáveis longos. Para criar esses nomes, precisamos substituir espaços por underscores em frases ou partes de frases.

Crie uma função make_variable_name que:

Receba uma string words e um inteiro number_of_words.
Retorne um nome de variável formado pelas primeiras palavras number_of_words, separadas por underscores.
Por exemplo:

make_variable_name("x", 1) # "x"
make_variable_name("a plus b problem", 3) # "a_plus_b"
make_variable_name("my favorite variable name is x", 3) # "my_favorite_variable"
"""

def make_variable_name(words: str, number_of_words: int) -> str:
    # quebrar a string em espaços e armazenar na lista
    if number_of_words == 0:
        return ""
    words_list = words.split()
    # declarar uma string com o primeiro item da lista quebrada
    variable_name = str(words_list[0])
    # fazer um for de concatenação de string
    for item in range(1, number_of_words):
        variable_name += "_" + words_list[item]
    return variable_name

print(make_variable_name("a plus b problem", 3))