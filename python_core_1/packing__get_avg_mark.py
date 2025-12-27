def get_average_mark(name: str, *args) -> str:
    print(f"{name} got {round(sum([*args])/len([*args]))}")


print(get_average_mark("Oleksii", 12, 10, 11, 11, 11))
print(get_average_mark("Emile", 12, 2, 12, 12, 12, 12, 12, 12, 12))