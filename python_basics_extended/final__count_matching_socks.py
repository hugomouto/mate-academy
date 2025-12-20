def count_matching_socks(colors: list) -> int:
    socks_dict = {}
    pairs_number = 0
    for item in colors:
        socks_dict[item] = colors.count(item)
    print(socks_dict)
    for item in socks_dict:
        pairs_number += socks_dict[item] // 2
    return pairs_number

print(count_matching_socks([10,10,10,10,10,10]))
print(count_matching_socks([10, 20, 30, 10, 20, 60]))