def calculate_guests(guests_input: str) -> int | str:
    number = ""
    for letter in guests_input:
        if number != "" and letter.isnumeric() == False:
            break
        elif letter.isnumeric():
            number += letter
    if number == "" or number == "0":
        return "not a number"
    return int(number)

print(calculate_guests("I think 5 guests"))
print(calculate_guests("There will be 71 or 9 guys"))