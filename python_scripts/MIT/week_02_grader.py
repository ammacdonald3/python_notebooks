import math


def polysum(n, s):
    """
    Polysum calculates sum of the area of a polygon plus the perimeter squared
    Arguments:
    n = number of sides
    s = length of each side
    Output is rounded to the fourth decimal
    """
    area = (0.25 * n * s**2) / (math.tan(math.pi / n))
    perimeter_squared = (s * n)**2
    return round((area + perimeter_squared), 4)
