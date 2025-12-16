"""
Imagine que estamos fazendo limonada para amigos. O número de porções que podemos fazer depende da quantidade de
açúcar e água que temos. Cada porção requer 500 ml de água e 100 g de açúcar.

Crie uma função make_lemonade() que:

Receba dois números, sugar_grams e water_liters.
Retorne o número de porções que podemos fazer, onde:
Se não houver água, não podemos fazer limonada — retorne "NaN".
Por exemplo:

make_lemonade(500, 2) retorna 4 porções, já que 2 litros de água fazem 4 porções.
make_lemonade(600, 6) retorna 6 porções, pois 600g de açúcar nos limita a 6 porções.
make_lemonade(300, 0) retorna "NaN" porque sem água não há limonada.
💡 Use float("nan") para "NaN" e a função built-in min. Para mais detalhes, acesse este artigo do GeeksforGeeks.
"""

def make_lemonade(sugar_grams: int, water_liters: int) -> int:
    total_water = water_liters * 2
    gram_count = sugar_grams // 100
    if water_liters == 0:
        return float("nan")
    elif total_water < 0.5:
        return 0
    else:
        return min([total_water, gram_count])

print(make_lemonade(500,2))