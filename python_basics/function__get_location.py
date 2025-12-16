def get_location(coordinates, commands):
    for comand in commands:
        if comand == "forward":
            coordinates[1] += 1
        if comand == "back":
            coordinates[1] -= 1
        if comand == "right":
            coordinates[0] += 1
        if comand == "left":
            coordinates[0] -= 1
    return coordinates
print(get_location([2, 3], ["back", "back", "back", "right"]))