def find_smaller_digits(ls: list) -> list:
    result_list = []
    for index,number in enumerate(ls):
        number_count = 0
        for number_in in ls[index+1:]:
            if number > number_in:
                number_count += 1
        result_list.append(number_count)
    return result_list

print(find_smaller_digits([5, 4, 3, 2, 1]))
print(find_smaller_digits([1, 2, 0]))