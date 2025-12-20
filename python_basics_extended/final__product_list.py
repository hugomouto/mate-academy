def product_list(numbers: list) -> list:
    list_result = []
    for index, number in enumerate(numbers):
        temp_value = 1
        for sub_number in numbers:
            temp_value *= sub_number
        temp_value = temp_value // number
        list_result.append(temp_value)
    return list_result