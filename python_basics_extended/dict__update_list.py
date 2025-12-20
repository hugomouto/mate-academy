""""
O banco de dados falhou. Alguns usuários perderam os valores do campo first_name, mas o user possui um campo full_name, então podemos restaurar o first_name.

Crie uma função restore_names que:

Receba uma lista de users.
Restaura o first_name para os usuários que estão com o valor ausente ou incorreto, com base no campo full_name.
Se o campo first_name estiver presente, mas incorreto (ou seja, não corresponder ao full_name), atualize-o com o valor correto vindo de full_name.
Não retorne nada.
"""

def restore_names(users: list) -> None:
    # for loop iterando cada item
    for user in users:
        # variável pra armazenar nome a partir do split - split_first_name
        split_first_name = user["full_name"].split()[0]
        # if user["first_name"] != split_firt_name
        if "first_name" in user:
            if user["first_name"] != split_first_name:
                user["first_name"] = split_first_name
        else:
            user.update({"first_name": split_first_name})