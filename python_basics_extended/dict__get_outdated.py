"""
robots = [
  { "core_version": 9 },
  { "core_version": 13 },
  { "core_version": 16 },
  { "core_version": 9 },
  { "core_version": 14 },
]

get_outdated(robots, 10) # [0, 3]
get_outdated(robots, 14) # [0, 1, 3]
get_outdated(robots, 8) # []
get_outdated(robots, 18) # [0, 1, 2, 3, 4]
"""


def get_outdated(robots: list, new_version: int) -> list:
    # nova lista
    new_list = []
    # for robot in robots:
    for index, robot in enumerate(robots):
        if robot["core_version"] < new_version:
            new_list.append(index)
    return new_list

robots_list = [
  { "core_version": 9 },
  { "core_version": 13 },
  { "core_version": 16 },
  { "core_version": 9 },
  { "core_version": 14 },
]

print(get_outdated(robots_list,18))