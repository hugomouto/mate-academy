class ListStatistics:
    def __init__(self, numbers: list = []) -> None:
        self.__numbers = numbers

    def __get_min_value(self) -> int:
        return min(self.__numbers)

    def __get_max_value(self) -> int:
        return max(self.__numbers)

    def __get_average(self) -> int:
        return sum(self.__numbers) / len(self.__numbers)

    def __get_median(self) -> float:
        ordered_list = sorted(self.__numbers)
        value_1 = ordered_list[len(ordered_list) // 2]
        if len(ordered_list) % 2 == 0:
            value_2 = ordered_list[(len(ordered_list) // 2) - 1]
            return (value_1 + value_2) / 2
        return value_1

    def calculate_statistics(self) -> dict:
        return {
            "min_value": self.__get_min_value(),
            "max_value": self.__get_max_value(),
            "average": self.__get_average(),
            "median": self.__get_median()
        }
