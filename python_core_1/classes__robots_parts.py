"""
robots parts


Você trabalha em uma fábrica de robôs. O projetista desenvolveu um plano para uma nova oficina de fabricação de robôs. Mas, para iniciar a produção, você precisa primeiro calcular o número de peças idênticas a serem fabricadas.

Você tem uma classe Robot. Seu método __init__ recebe o número de peças das quais os robôs são feitos: wheels, gears e pistons, e os armazena nas propriedades de acordo.

Escreva uma função robots_parts que:

Recebe uma lista de instâncias da classe Robot.
Calcula a soma das partes de diferentes tipos
Grava em um dicionário com as chaves: 'wheels', 'gears' e 'pistons'
Retorna o resultado.

Exemplo:

robots = [
  Robot(wheels=10, gears=18, pistons=16),
  Robot(wheels=4, gears=8, pistons=8),
  Robot(wheels=22, gears=17, pistons=30),
]

robots_parts(robots) == {
  'wheels': 36,
  'gears': 43,
  'pistons': 54
}
"""

class Robot:
    def __init__(self, wheels: int, gears: int, pistons: int) -> None:
        self.wheels = wheels
        self.gears = gears
        self.pistons = pistons


def robots_parts(robots: list) -> dict:
    total_parts = {
        "wheels": 0,
        "gears": 0,
        "pistons": 0
    }
    for robot in robots:
        total_parts["wheels"] += robot.wheels
        total_parts["gears"] += robot.gears
        total_parts["pistons"] += robot.pistons
    return total_parts

robots = [
  Robot(wheels=10, gears=18, pistons=16),
  Robot(wheels=4, gears=8, pistons=8),
  Robot(wheels=22, gears=17, pistons=30),
]

print(robots_parts(robots))