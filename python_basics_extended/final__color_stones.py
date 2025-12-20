def color_stones(stones: str) -> int:
    spare_stone_count = 0
    for index,char in enumerate(stones):
        if index + 1 < len(stones) :
            next_char = stones[index + 1]
            if char == next_char:
                spare_stone_count += 1
    return spare_stone_count

print(color_stones("RRGB"))
print(color_stones("RRGGB"))
print(color_stones("RRRRGB"))
print(color_stones("RGBRGBRGGB"))
print(color_stones("RGGRGBBRGRR"))
print(color_stones("RRRRGGGGBBBB"))