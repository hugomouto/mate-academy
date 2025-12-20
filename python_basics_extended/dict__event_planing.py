"""
Estamos organizando uma grande exposição de tecnologia e moda e temos listas separadas de participantes para cada departamento. Primeiro, usaremos dois métodos de conjuntos:

union - para obter a lista de todos os visitantes únicos da exposição.
intersection - para encontrar participantes interessados tanto em tecnologia quanto em moda.
symmetric_difference — para identificar participantes interessados apenas em uma das áreas.
Depois — a função event_planning, que deve retornar um tuple com dois conjuntos:

O primeiro conjunto contém os participantes interessados em ambas as áreas.
O segundo conjunto contém os que preferem apenas uma das áreas.
Por exemplo:

electronics_attendees = {"Alex", "Maria", "John"}
clothing_attendees = {"John", "Sophia", "Maria", "Mike"}

event_planning(electronics_attendees, clothing_attendees) == ({"John", "Maria"}, {"Alex", "Sophia", "Mike"})
"""

def event_planning(electronics_attendees: set, clothing_attendees: set) -> tuple[set, set]:
    attendees_union = electronics_attendees | clothing_attendees
    attendees_intersection = electronics_attendees & clothing_attendees
    final_tuple =(attendees_intersection, attendees_union - attendees_intersection)
    return final_tuple
