class Robot:
    def __init__(self, name: str) -> None:
        self.name = name
        self.partner = None


def pair_robots(robot_list: list) -> tuple:
    robot1 = Robot(robot_list[0])
    robot2 = Robot(robot_list[1])
    robot1.partner = robot2
    robot2.partner = robot1
    return (robot1, robot2)

