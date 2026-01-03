from typing import Iterable, TypeVar
T = TypeVar("T")


class Cycle:
    def __init__(self, iterable: Iterable[T]) -> None:
        self.iterable = iterable

    def __iter__(self) -> int:
        self.it = 0
        return self

    def __next__(self) -> T:
        if len(self.iterable) == 0:
            raise StopIteration
        if self.it >= len(self.iterable):
            self.it = 0
            result = self.iterable[self.it]
            self.it += 1
            return result
        result = self.iterable[self.it]
        self.it += 1
        return result


iterator = iter(Cycle("abc"))
print(next(iterator)) # a
print(next(iterator)) # b
print(next(iterator)) # c
print(next(iterator)) # a
print(next(iterator)) # b
print(next(iterator)) # c
print(next(iterator)) # a

