"""
Tarefa

admin required


Você tem uma função send_secure_information que recebe um dicionário user. Ela divulga informações secretas para o usuário.

Escreva um decorador admin_required que verifique o atributo de usuário 'is_admin'. Se for False, ele exibe uma mensagem de negação, conforme mostrado no exemplo:

@admin_required
    def send_secure_information(user: dict) -> None:
        print(f"{user['name']}, site's secure code is 'SecUR43Esit78Eco90DE'")

send_secure_information({'name': 'Administrator', 'is_admin': True})
# Administrator, site's secure code is 'SecUR43Esit78Eco90DE'

send_secure_information({'name': 'User1234', 'is_admin': False})
# You are not allowed to see this information!
"""

from typing import Callable

def admin_required(func: Callable) -> Callable:
    def wrapper (user: dict):
        if user["is_admin"]:
            print(f"{user['name']}, site's secure code is 'SecUR43Esit78Eco90DE'")
        else:
            print(f"You are not allowed to see this information!")
    return wrapper

@admin_required
def send_secure_information(user: dict) -> None:
    return admin_required





send_secure_information({'name': 'Administrator', 'is_admin': True})