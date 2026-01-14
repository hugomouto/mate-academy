class Grade:
    def __init__(self, minvalue=2, maxvalue=12):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def __set_name__(self, owner, name):
        self.protected_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.protected_name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Grade should be integer")

        if not (self.minvalue <= value <= self.maxvalue):
            raise ValueError(
                f"Grade should not be less than {self.minvalue} and greater than {self.maxvalue}"
            )

        instance.__dict__[self.protected_name] = value


class SchoolDiary:
    math = Grade()
    history = Grade()
    literature = Grade()

    def __init__(self, math, history, literature):
        self.math = math
        self.history = history
        self.literature = literature
