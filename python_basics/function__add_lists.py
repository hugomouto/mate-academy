def get_lists_sum(ls1, ls2):
    sum_ls1 = 0
    sum_ls2 = 0
    for item in range(len(ls1)):
        sum_ls1 += ls1[item]
        sum_ls2 += ls2[item]
    return sum_ls1 + sum_ls2


print(get_lists_sum([1, 2], [3, 4]))