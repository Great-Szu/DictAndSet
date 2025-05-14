def time_calculator(hours: list[int], minutes: list[int]) -> float:
    """
    Adds hours and minutes together and returns total time in hours.
    :param hours: List of hour values.
    :param minutes: List of minute values.
    :return: Total time in hours (as a float).
    """
    total_minutes = sum(hours) * 60 + sum(minutes)
    return total_minutes / 60

godzinki = [2, 4, 4, 3, 5]
minutki = [14, 35, 30, 13, 45, 58]

print(time_calculator(godzinki, minutki))