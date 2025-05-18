def time_calculator(hours: list[int], minutes: list[int]) -> float:
    """
    Adds hours and minutes together and returns total time in hours.
    :param hours: List of hour values.
    :param minutes: List of minute values.
    :return: Total time in hours (as a float).
    """
    total_minutes = sum(hours) * 60 + sum(minutes)
    return total_minutes / 60

h = []
m = [556]

print(time_calculator(h, m))