def make_stickers(details_count, robot_part):
    sticker_list = []
    for detail in range(1,details_count+1):
        sticker_list.append(f"{robot_part} detail #{detail}")
    return sticker_list

print(make_stickers(3, "Body"))