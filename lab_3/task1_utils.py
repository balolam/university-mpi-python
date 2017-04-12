import numpy as np


def multiply_arrs_python(a, b):
    len_ = a.size
    res_ = np.zeros(len_)
    ind_ = 0

    while ind_ < len_:
        res_[ind_] = a[ind_] * b[ind_]
        ind_ = ind_ + 1

    return res_


# noinspection PyShadowingNames
def multiply_arrs_c(a, b): return np.multiply(a, b)


# noinspection PyShadowingNames
def multiply_arrs(a, b): return multiply_arrs_c(a, b)
