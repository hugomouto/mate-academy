def get_leaders(numbers: list) -> list:
    leaders_list = []
    for index in range(0, len(numbers)):
        if numbers[index] > sum(numbers[index +1:]):
            leaders_list.append(numbers[index])
    return leaders_list


leaders_list = [1, 2, 3, 4, 0]
print(leaders_list[0:])
print("-------")
print(get_leaders([1, 2, 3, 4, 0]))
print(get_leaders([16, 17, 4, 3, 5, 2]))