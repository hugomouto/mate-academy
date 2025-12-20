def sum_dicts(*dicts) -> dict:
    final_dict = {}
    for item in dicts:
        final_dict.update(item)
    for item in final_dict:
        final_dict[item] = 0
    for item in final_dict:
        for one_dict in dicts:
            for sub_item in one_dict:
                if item == sub_item:
                    final_dict[item] += one_dict[sub_item]
    return final_dict

first = {"a": 2, "b": 4}
second = {"a": 2, "b": 10}
third = {"d": -5}

print(sum_dicts(first, second, third))

"""for item in final_dict:
    for dict in dicts:
        for sub_item in dict:
            if item == sub_item:
                final_dict[item] += dict[sub_item]
            else:
                final_dict[sub_item] = dict[sub_item]"""