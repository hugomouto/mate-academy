def remove_vowels(document):
    new_string = ""
    document = document.lower()
    forbidden_vowels = "aeiou"
    for letter in document:
        if letter not in forbidden_vowels:
            new_string += letter
    return new_string

print(remove_vowels("captain"))
