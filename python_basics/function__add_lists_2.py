def get_lists_sum(ls1, ls2):
    sum_ls1 = 0
    sum_ls2 = 0
    new_list = []
    for item in range(len(ls1)):
        new_list.append(ls1[item]+ls2[item])
    return new_list


print(get_lists_sum([1, 2], [3, 4]))