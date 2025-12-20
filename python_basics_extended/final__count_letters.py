"""
Crie uma função count_letters_in_string que:

Receba uma string string.
Retorne um dicionário com as letras da string como chaves e suas contagens como valores.
Por exemplo:

count_letters_in_string("arithmetics") == {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}


"""

def count_letters_in_string(string: str) -> dict:
    lower_string = string.lower()
    new_object = {}
    for char in lower_string:
        new_object[char] = lower_string.count(char)
    return new_object
