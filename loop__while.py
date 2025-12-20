def detect_lowercase_words() -> None:
    while True:
        word = input()
        upper_letter = []
        if word == "exit":
            break
        for char in word:
            if char.isupper():
                upper_letter.append(True)
            else:
                upper_letter.append(False)
        if not any(upper_letter):
            print(f"{word} detected")

detect_lowercase_words()