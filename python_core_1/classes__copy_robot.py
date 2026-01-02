"""
Você trabalha em uma fábrica de robôs. Você inspecionou os robôs antigos e selecionou os modelos que serão úteis no futuro. No entanto, há um problema: esses robôs são tão antigos que sua documentação foi perdida há muito tempo. E agora é seu trabalho gerenciar a cópia desses robôs.

Você tem uma classe Robot. Seu metodo __init__ obtém os valores model, constructor e serial_no e os armazena nas propriedades de acordo com eles.

Escreva uma função copy_robot que receba uma instância da classe Robot e retorna uma cópia de robot, mas com o serial_no aumentado em um.

Exemplo:

robot = Robot('g135', 'Alex', 1664)
robot_copy = copy_robot(robot)

robot_copy is robot == False
robot_copy.model == 'g135'
robot.serial_no == 1664
robot_copy.serial_no == 1665
"""

class Robot:
    def __init__(self, model: str, constructor: str, serial_no: int) -> None:
        self.model = model
        self.constructor = constructor
        self.serial_no = serial_no


def copy_robot(robot: Robot) -> Robot:
    robot_copy = Robot(robot.model, robot.constructor, robot.serial_no)
    robot_copy.serial_no = robot.serial_no + 1
    return robot_copy
