class Volume:
    def __get__(self, instance, owner):
        return instance.length * instance.width * instance.height


class Box:
    def __init__(self, length, width, height) -> None:
        self.length = length
        self.width = width
        self.height = height

    volume = Volume()

small_box = Box(2, 4, 6)
print(small_box.volume)