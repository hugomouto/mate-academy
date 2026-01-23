from collections import Counter
from typing import Any

def find_mode(ls: list):
    if not isinstance(ls, list):
        raise TypeError("ls must be a list")
    if len(ls) == 0:
        raise ValueError("ls must be non-empty")
    count = Counter(ls)
    most_common_item = count.most_common(1)[0][0]
    return most_common_item

print(find_mode([5, "hello", 12, 33, "a", 12, "a", "a"]))