"""
Estamos planejando uma ida ao mercado e precisamos de uma lista de compras. Para facilitar a leitura, todos os itens devem ser unidos em uma única string, separados por vírgula.

Crie a função create_shopping_list(), que:

Receba uma lista de strings items, onde cada string é um item da nossa lista de compras.
Use o método join() para criar uma única string a partir de todos os itens, separados por espaço e vírgula.
Por exemplo:

create_shopping_list(["apples", "bananas", "bread"]) # "apples, bananas, bread"
create_shopping_list(["milk"]) # "milk"
"""
def create_shopping_list(items: list) -> str:
    return ", ".join(items)

print(create_shopping_list(["apples", "bananas", "bread"]))