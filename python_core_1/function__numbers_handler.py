def new_number(number: int) -> None:
    print(f"Received a new number: {number}")


def is_positive(number: int) -> None:
    if number > 0:
        print(f"{number} is a positive number")
    elif number < 0:
        print(f"{number} is a negative number")
    else:
        print("Zero")


def print_bye(number: int) -> None:
    print("Bye!")


def numbers_handler(
    numbers: list,
    before: callable = new_number,
    action: callable = is_positive,
    after: callable = print_bye,
) -> None:
    for number in numbers:
        before(number)
        action(number)
        after(number)
