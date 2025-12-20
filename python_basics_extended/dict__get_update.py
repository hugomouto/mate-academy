"""
Imagine que possuímos uma loja e mantemos uma lista de inventário como um dicionário, onde as chaves são os nomes dos produtos e os valores são as quantidades em estoque. Queremos verificar rapidamente a disponibilidade de um determinado produto e sua quantidade sem causar um erro caso o produto não esteja em estoque.

Crie uma função check_item_stock que:

Receba a lista de inventário e o item_name para verificar.
Use o método get para obter a quantidade do produto em estoque.
Se o produto estiver na lista, retorne True, caso contrário — False.
Por exemplo:

inventory = {"apples": 30, "bananas": 45}
item_name = "oranges"

check_item_stock(inventory, item_name) # False
"""

def check_item_stock(inventory: dict, item_name: str) -> bool:
    if inventory.get(item_name, 0) > 0:
        return True
    else:
        return False

print(check_item_stock({"apples": 30, "bananas": 45},"oranges"))