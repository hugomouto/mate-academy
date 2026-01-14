from decimal import Decimal


class NumberInfo:
    def __init__(self, number: float) -> None:
        self._number = number

    @property
    def number(self) -> float:
        return self._number

    @number.setter
    def number(self, value: float) -> None:
        self._number = value

    @property
    def len_digits(self) -> int:
        return len(str(int(abs(self._number))))

    @property
    def is_integer(self) -> bool:
        return isinstance(self._number, int) or (
            isinstance(self._number, float) and self._number.is_integer()
        )

    @property
    def is_float(self) -> bool:
        return isinstance(self._number, float) and not self._number.is_integer()

    @property
    def decimal(self) -> int:
        if not self.is_float:
            return 0

        decimal_number = Decimal(str(self._number)).normalize()

        if decimal_number == decimal_number.to_integral():
            return 0

        return abs(decimal_number.as_tuple().exponent)

    @property
    def is_positive(self) -> bool:
        return self._number > 0

    @property
    def is_natural(self) -> bool:
        return self.is_positive and self.is_integer

    @property
    def is_prime(self) -> bool:
        if not self.is_integer:
            return False

        n = int(self._number)
        if n < 2:
            return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
