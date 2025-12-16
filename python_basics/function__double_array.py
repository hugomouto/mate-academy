def double_power(current_powers):
    new_list = []
    for item in range(len(current_powers)):
        new_list.append(current_powers[item]*2)
    return new_list
print(double_power([100, 150, 200, 220]))

# Versão menos verbosa

def double_power2(current_powers):
    new_list = []
    for item in current_powers:
        new_list.append(item*2)
    return new_list
print(double_power2([100, 150, 200, 220]))