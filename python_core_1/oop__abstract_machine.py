from abc import ABC, abstractmethod

class Machine(ABC):
    @abstractmethod
    def do_work(self):
        pass

    @abstractmethod
    def stop_work(self):
        pass


class Truck(Machine):
    def do_work(self):
        print(f"{self.__class__.__name__} starts working")

    def stop_work(self):
        print(f"{self.__class__.__name__} stopped working")

class Bulldozer(Machine):
    def do_work(self):
        print(f"{self.__class__.__name__} starts working")

    def stop_work(self):
        print(f"{self.__class__.__name__} stopped working")

class Excavator(Machine):
    def do_work(self):
        print(f"{self.__class__.__name__} starts working")

    def stop_work(self):
        print(f"{self.__class__.__name__} stopped working")

def build():
    machines_list = [Truck(), Bulldozer(), Excavator()]
    [machine.do_work() for machine in machines_list]
    [machine.stop_work() for machine in machines_list]

build()