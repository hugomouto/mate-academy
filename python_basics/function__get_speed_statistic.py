from math import floor
import math

def get_speed_statistic(test_results):
    speed_sum = 0
    if len(test_results) == 1:
        result = [test_results[0], test_results[0], test_results[0]]
        return result

    elif len(test_results)<1:
        result = [0,0,0]
        return result

    else:
        low_speed = test_results[0]
        high_speed = test_results[0]
        # Detect high_speed
        for item in range(1,len(test_results)):
            if test_results[item] > test_results[item-1]:
                high_speed = test_results[item]
        # Detect low_speed
        for item in range(1,len(test_results)):
            if test_results[item] < test_results[item-1]:
                low_speed = test_results[item]

        # Calculate avg
        for item in range(len(test_results)):
            speed_sum += test_results[item]
        avg_speed = math.floor(speed_sum/len(test_results))
        result = [low_speed, high_speed, avg_speed]
        return result
print(get_speed_statistic([8, 9, 3, 12]))
print(get_speed_statistic([10, 10, 11, 9, 12, 8]))
print(get_speed_statistic([10]))
print(get_speed_statistic([]))

