import math

def RastriginFunction(x,y):
    a = 10
    dimension = len(x)
    sum_part = sum([(xi ** 2 - a * math.cos(2 * math.pi * xi)) for xi in x])
    return a * dimension + sum_part
