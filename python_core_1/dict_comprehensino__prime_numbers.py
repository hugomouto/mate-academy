def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_numbers(numbers: list) -> dict:
    return {num: is_prime(num) for num in numbers}

numbers = [19]
print(prime_numbers(numbers))  # {19: True}

numbers = [3, 6, 12, 17]
print(prime_numbers(numbers)) # {3: True, 6: False, 12: False, 17: True}
