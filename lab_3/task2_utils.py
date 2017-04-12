import numpy as np


# noinspection PyShadowingNames
def max_el_python(arr):
    length = len(arr)

    if length > 0:
        max_el = arr[0]
        index = 1

        while index < length:
            el = arr[index]

            if max_el < el:
                max_el = el

        return max_el
    else:
        return None


# noinspection PyShadowingNames
def max_el_c(arr): return np.nanmax(arr)


# noinspection PyShadowingNames
def max_el(arr): return max_el_c(arr)