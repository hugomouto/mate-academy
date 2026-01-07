def fibonacci_generator(numbers: int) -> int:
    fib_list = [0, 1]
    for number in range(numbers):
        if number < 2:
            yield fib_list[number]
        else:
            fib_list.append(fib_list[number - 1] + fib_list[number - 2])
            yield fib_list[-1]