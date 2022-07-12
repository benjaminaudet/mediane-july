import math


def compute_cone_volume(r, h):
    return (math.pow(r, 2) * h * math.pi) / 3


print(compute_cone_volume(5, 30))
