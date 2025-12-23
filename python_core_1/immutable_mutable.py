def create_dictionary(*args):
    result_dict = {}
    for index, arg in enumerate(args):
        if isinstance(arg, (list, set, dict)):
            print(f"Cannot add {arg} to the dict!")
        else:
            result_dict[arg] = index
    return result_dict

print(create_dictionary(7, 1, 3))
print(create_dictionary(3, [1, 2], 5))