"""
Estamos desenvolvendo um jogo de "Sim ou Não". Crie a função yes_or_no que:

Retorne "Yes" se o valor do argumento for True, caso contrário — "No".
Retorne "No" se o word_request for especificado como "no".
Por exemplo:

yes_or_no("yes") == "Yes"
yes_or_no("no") == "No"
yes_or_no(1) == "Yes"
yes_or_no(0) == "No"
yes_or_no([]) == "No"
yes_or_no([""]) == "Yes"
yes_or_no("") == "No"
"""

def yes_or_no(word_request: str) -> str:
    if word_request and word_request != "no":
        return "Yes"
    else:
        return "No"


print(yes_or_no("yes"))
print(yes_or_no("no"))
print(yes_or_no(1))
print(yes_or_no(0))
print(yes_or_no([]))
print(yes_or_no([""]))
print(yes_or_no(""))