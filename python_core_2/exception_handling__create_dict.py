def create_dict(keys_tuple: tuple) -> dict:
    new_dict = {}
    for index, elem in enumerate(keys_tuple):
        try:
            new_dict[elem] = index
        except TypeError:
            print(f"Cannot add {elem} to the dict!")
    return new_dict
