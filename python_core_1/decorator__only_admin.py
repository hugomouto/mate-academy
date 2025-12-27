"""
only admin


Você tem uma função create_permissions que recebe uma lista de dicionários com usuários e exibe uma mensagem sobre as permissões criadas.

Sua tarefa é escrever um decorador only_admin que recebe o primeiro argumento users passado para a função. Em seguida, ele filtra apenas os usuários com is_admin = True e chama a função decorada apenas para esses usuários.

💡 O campo is_admin pode não ser apenas do tipo bool.

Exemplo:

@only_admin
def create_permissions(users: list) -> None:
    for user in users:
        print(f'Creating permissions for {user["username"]}')

users = [
     {'username': 'admin', 'is_admin': True},
     {'username': 'moderator_a11', 'is_admin': True},
     {'username': 'custom_user1', 'is_admin': False},
     {'username': 'custom_user2', 'is_admin': False},
     {'username': 'admin_2nd', 'is_admin': True},
]

create_permissions(users)
# Creating permissions for admin
# Creating permissions for moderator_a11
# Creating permissions for admin_2nd
"""

def only_admin(func: callable) -> callable:
    def inner(users: list) -> list:
        admins = []
        for user in users:
            if user["is_admin"] is True:
                admins.append(user)
        func(admins)
    return inner


@only_admin
def create_permissions(users: list) -> None:
    for user in users:
        print(f'Creating permissions for {user["username"]}')

users = [
    {"username": "admin", "is_admin": True},
    {"username": "user2", "is_admin": False},
    {"username": "user123", "is_admin": "True"},
    {"username": "user123", "is_admin": 1},
    {"username": "user123", "is_admin": 0},
    {"username": "admin001", "is_admin": True},
]

create_permissions(users)