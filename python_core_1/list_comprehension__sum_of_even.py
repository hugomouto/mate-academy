def sum_of_even_numbers(numbers: list) -> int:
    return sum([num for num in numbers if num % 2 == 0])

print(sum_of_even_numbers([2, 11, 2, 4]))