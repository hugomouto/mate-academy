"""
Crie uma função get_century() que:

Receba um inteiro year.
Retorne o century correspondente a esse ano, onde:
year = 0 deve ser processado como o 1º ano (e o 1º século).
1800 pertence ao século 18, enquanto 1801 pertence ao século 19 (e assim por diante).
Por exemplo:

get_century(2001) == 21
get_century(0) == 1
get_century(1786) == 18
get_century(1500) == 15
"""

def get_century(year: int) -> int:
    int_n = year // 100
    float_n = year / 100
    if int_n < float_n < int_n +1 or year == 0:
        return int(int_n +1)
    else:
        return int(int_n)

print(get_century(2001))
print(get_century(0))
print(get_century(1786))
print(get_century(1500))