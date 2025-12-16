"""
O oráculo de Delfos nos enviou uma mensagem com os nomes das pessoas que têm a melhor chance de ganhar na loteria. Precisamos notificá-las imediatamente!

No entanto, a mensagem inclui espaços extras, e cada nome está separado por uma vírgula. Assim, nosso sistema tem dificuldades para extrair os nomes.

Crie uma função extract_names() que:

Receba uma string message com nomes separados por vírgulas e, possivelmente, com espaços extras.
Retorne uma lista de nomes sem espaços extras.
Por exemplo:

extract_names("Oleg") # ["Oleg"]
extract_names("Ivan,  Mark,  Sergey") # ["Ivan", "Mark", "Sergey"]
extract_names("Ivan,Mark,Sergey") # ["Ivan", "Mark", "Sergey"]
"""

def extract_names(message: str) -> list:
    split_list = message.split(",")
    clean_list = []
    for item in split_list:
        clean_list.append(item.strip())
    return clean_list


print(extract_names("Ivan,  Mark,  Sergey"))
