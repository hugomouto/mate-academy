"""
Crie uma função weekday_order que:

Receba uma string representando um dia da semana (por exemplo, "Monday").
Retorne o número correspondente (0 para Monday, 1 para Tuesday, até 6 para Sunday).
Em seguida, crie uma função sort_weekdays que:

Receba uma lista de dias da semana em ordem aleatória.
Retorne os dias na ordem correta de Monday a Sunday, onde:
weekday_order será usado como chave.
Por exemplo:

sort_weekdays(["Monday"]) # ["Monday"]
sort_weekdays(["Saturday", "Wednesday"]) # ["Wednesday", "Saturday"]
"""

def weekday_order(weekday: str) -> int:
    # write your code here
    if weekday == "Monday":
        return 0
    elif weekday == "Tuesday":
        return 1
    elif weekday == "Wednesday":
        return 2
    elif weekday == "Thursday":
        return 3
    elif weekday == "Friday":
        return 4
    elif weekday == "Saturday":
        return 5
    else:
        return 6

def sort_weekdays(weekdays: list) -> list:
    sorted_weekdays = sorted(weekdays, key=weekday_order)
    return sorted_weekdays

print(sort_weekdays(["Saturday", "Wednesday"]))