"""
Estamos organizando uma conferência e organizando os assentos para os participantes em um auditório. O auditório é composto por fileiras e assentos por fileira. Nossa tarefa é imprimir um plano de assentos, marcando os números das fileiras e os assentos em cada fileira.

Crie uma função seating_arrangement que:

Receba o número de rows (fileiras) e o número de seats_per_row (assentos por fileira).
Use loops aninhados para imprimir os números das fileiras e assentos, onde:
O loop externo itera pelas rows.
O loop interno itera pelos assentos em cada fileira. No resultado final, o row number para cada fileira deve vir primeiro, e os números dos assentos nessa fileira — depois. Aqui está um exemplo de saída para um auditório com 3 rows e 4 assentos por fileira:
seating_arrangement(3, 4) == [
    "Row 1: Seat 1, Seat 2, Seat 3, Seat 4",
    "Row 2: Seat 1, Seat 2, Seat 3, Seat 4",
    "Row 3: Seat 1, Seat 2, Seat 3, Seat 4"
]
"""

def seating_arrangement(rows: int, seats_per_row: int) -> list[str]:
    seats_list = []
    for row in range(0, rows):
        seats_list.append(f"Row {row + 1}: ")
        for seat in range(0, seats_per_row):
            seats_list[row] += f"Seat {seat + 1}, "
    if seats_per_row > 0:
        for item in range(0, len(seats_list)):
            seats_list[item] = seats_list[item].rstrip(", ")
    return seats_list

print(seating_arrangement(3,4))
print(seating_arrangement(3,0))