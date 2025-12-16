# Find and fix the issue

def calculate_average(numbers):
    total = 0
    count = len(numbers)
    for number in numbers[1:]:
        total += number

    if count > 0:
        return total / count

    return 0

print(calculate_average([1,2,3,4,5]))
