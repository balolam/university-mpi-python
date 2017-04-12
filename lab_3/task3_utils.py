import numpy as np


# noinspection PyShadowingNames
def sum_els_python(arr):
    length = len(arr)

    if length > 0:
        sum_els = 0
        index = 1

        while index < length:
            sum_els = sum_els + arr[index]

        return sum_els
    else:
        return 0


# noinspection PyShadowingNames
def sum_els_c(arr): return np.nansum(arr)


# noinspection PyShadowingNames
def sum_els(arr): return sum_els_c(arr)