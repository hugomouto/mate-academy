"""
Recebemos uma string com a data e hora de um evento no formato "YYYY-MM-DD HH:MM:SS", mas precisamos apenas da data para um relatório.

Vamos criar uma função get_date_from_datetime() que:

Receba uma datetime_string com data e hora.
Use slicing para obter a substring da data.
Retorne a substring da data (os primeiros 10 caracteres).
Por exemplo:

get_date_from_datetime("2023-12-01 15:30:00") # "2023-12-01"
get_date_from_datetime("2024-01-20 08:15:45") # "2024-01-20"
"""

def get_date_from_datetime(datetime_string: str) -> str:
    return datetime_string[:10]

print(get_date_from_datetime("2023-12-01 15:30:00"))
