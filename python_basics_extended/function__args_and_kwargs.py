def multiply_numbers(*a_numbers,**b_numbers):
    numbers_list = []
    kwarg_list = b_numbers.values()
    if a_numbers or b_numbers:
        for number in a_numbers:
            if type(number) == int:
                numbers_list.append(number)
        if b_numbers:
            for item in kwarg_list:
                if len(numbers_list) < 2:
                    numbers_list.append(item)
        if len(numbers_list) == 1:
            return numbers_list[0]
        return numbers_list[0] * numbers_list[1]
    else:
        return 1

print(multiply_numbers())
print(multiply_numbers(2, 3))
print(multiply_numbers(b=5))
print(multiply_numbers(4, 3, "string", []))
print(multiply_numbers(1, 3, "string", k=22))

