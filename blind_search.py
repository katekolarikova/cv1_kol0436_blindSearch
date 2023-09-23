import random

from function_definitions.ackley_definition import AckleyFunction


def BlindSearch(func, iterationCount,lowerLimitX, upperLimitX, lowerLimitY, upperLimitY):
    maximumValue = func(random.uniform(lowerLimitX, upperLimitX), random.uniform(lowerLimitY, upperLimitY))
    maximumX = None
    maximumY = None
    pointHistory = []
    pointHistory.append((maximumX, maximumY, maximumValue))

    for i in range(iterationCount):
        x = random.uniform(lowerLimitX, upperLimitX)
        y = random.uniform(lowerLimitY, upperLimitY)
        value = func(x, y)
        if value < maximumValue:
            maximumValue = value
            maximumX = x
            maximumY = y
            pointHistory.append((maximumX, maximumY, maximumValue))

    return pointHistory
    