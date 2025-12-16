"""
Precisamos enviar nosso número de cartão de crédito para um amigo, escondendo todos os dígitos, exceto os últimos 4, por razões de segurança.

Crie uma função mask_card_number() que:

Receba uma string card_number contendo o número do cartão.
Use multiplicação de strings e slicing para criar o número mascarado.
Retorne o número do cartão mascarado com:
Os primeiros 12 caracteres substituídos por "*".
Os últimos 4 caracteres inalterados.
Por exemplo:

mask_card_number("1234567890123456") == "**** **** **** 3456"
mask_card_number("5555444433331111") == "**** **** **** 1111"
"""

def mask_card_number(card_number: str) -> str:
    masked_string = ("*" * 4 + " ") * 3 + card_number[-4:]
    return masked_string

print(mask_card_number("1234567890123456"))