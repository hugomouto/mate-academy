def get_reversed_list(items: list) -> list:
    new_list = items.copy()
    new_list.reverse()
    return new_list

print(get_reversed_list([1,2,3,4,5]))