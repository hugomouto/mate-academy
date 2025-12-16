# Find and fix the issue

def find_max(numbers):
    if type(numbers) != list:
        return None
    else:
        max_num = numbers[0]
        for num in numbers:
            if max_num < num:
                max_num = num
        return max_num


print(find_max([1,3,2,6]))
print(find_max(2))