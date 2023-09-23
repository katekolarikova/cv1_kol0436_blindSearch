import math

import numpy as np


def RastriginFunction(X,Y):
    a = 10
    return (X**2 - 10 * np.cos(2 * np.pi * X)) + \
            (Y**2 - 10 * np.cos(2 * np.pi * Y)) + 20
