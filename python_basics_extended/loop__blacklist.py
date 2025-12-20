"""
Imagine que somos responsáveis pela segurança de um site e precisamos verificar uma lista de endereços de e-mail em relação a uma lista negra. Se um endereço for encontrado na lista negra, precisamos parar de verificar imediatamente.

Crie uma função check_emails_against_blacklist que:

Receba uma lista de emails e uma blacklist.
Itere pelos emails usando um loop for.
Se o endereço atual estiver na blacklist, retorne-o e pare de verificar usando break.
Se emails estiver vazia ou não estiver presente na blacklist, uma string vazia deve ser retornada.
Exemplo:

emails = ["user@example.com", "spam@blacklist.com", "anotheruser@example.com"]
blacklist = {"spam@blacklist.com", "banneduser@example.com"}

check_emails_against_blacklist(emails, blacklist) # "spam@blacklist.com"
"""

def check_emails_against_blacklist(emails: list[str], blacklist: set) -> str:
    if emails is False:
        return ""
    result = ""
    for email in emails:
        if email in blacklist:
            result = email
            break
    return result

print(check_emails_against_blacklist(["user@example.com", "spam@blacklist.com", "anotheruser@example.com"],{"spam@blacklist.com", "banneduser@example.com"}))


