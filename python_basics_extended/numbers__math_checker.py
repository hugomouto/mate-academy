"""
Crie uma função check_number que:

Analise um inteiro number com base em três critérios:
Ele é positivo?
Ele é par?
Ele é divisível por 10 sem resto?
Retorne uma lista com cada critério representado por True ou False.
Por exemplo:

check_number(3)  # [True, False, False], positive, not even, and does not divide by 10
check_number(10)  # [True, True, True], positive, even, and divides by 10
check_number(0)  # [False, True, True], 0 is not considered positive, but it is even and divides by 10
check_number(-1)  # [False, False, False], negative, not even, and does not divide by 10
"""

def check_number(number: int) -> list[bool]:
    # Declarar variável math_checker como lista vazia para receber análise
    is_positive = number > 0
    is_even = number % 2 == 0
    is_divisible_by_10 = number % 10 == 0
    math_check = [is_positive, is_even, is_divisible_by_10]

    
    return math_check


print(check_number(3))
print(check_number(10))
print(check_number(0))
print(check_number(-1))