class BoolConversionError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


def from_int(value: int) -> None:
    if not isinstance(value, int):
        raise TypeError
    if value == 1:
        return True
    if value == 0:
        return False
    raise ValueError


def from_str(value: str) -> None:
    if not isinstance(value, str):
        raise TypeError
    if value in ["True", "T", "1"]:
        return True
    if value in ["False", "F", "0"]:
        return False
    raise ValueError


def make_bool(value: bool) -> None:
    try:
        return from_int(value)

    except ValueError:
        # Valor inválido para int
        raise BoolConversionError(
            f"Cannot convert to the bool {value} value"
        )

    except TypeError:
        # Tipo não é int → tenta string
        try:
            return from_str(value)

        except ValueError:
            # Valor inválido para string
            raise BoolConversionError(
                f"Cannot convert to the bool {value} value"
            )

        except TypeError:
            # Tipo não é string
            raise BoolConversionError(
                f"Cannot convert to the bool {type(value)} type"
            )
