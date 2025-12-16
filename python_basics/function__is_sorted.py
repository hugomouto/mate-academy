def is_sorted(box_numbers):
    greater_than_previous = False
    if len(box_numbers) <= 1:
        greater_than_previous = True
    else:
        for number in range(1, len(box_numbers)):
            if box_numbers[number] >= box_numbers[number-1]:
                greater_than_previous = True
            else:
                greater_than_previous = False
                break
    return greater_than_previous


print(is_sorted([1,3,2]))