from __future__ import annotations
from typing import Iterator


class NumberIterator:
    def __init__(self, numbers: list) -> None:
        self.numbers = numbers

    def __iter__(self) -> NumberIterator:
        self.it = 0
        return self

    def __next__(self) -> int:
        if self.it >= len(self.numbers):
            raise StopIteration
        result = self.numbers[self.it]
        self.it += 1
        return result


def fetch_numbers(iterator: Iterator, number: int) -> list:
    new_list = []
    for i in range(number):
        new_list.append(next(iterator))
    return new_list

iter_ = iter(
  NumberIterator([1, 2, 3, 4, 5])
)

print(fetch_numbers(iterator=iter_, number=3))  # [1, 2, 3]

print(next(iter_))  # 4