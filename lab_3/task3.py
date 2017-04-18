from mpi4py import MPI

import numpy as np

from sys import argv

from lab_3.task3_utils import sum_els
from tools.mpi_helper import init, finalize


# noinspection PyShadowingNames
from tools.utils import current_time_millis, find_numpy_array_human_size, enum, track_time

array_size = int(argv[1])
tags = enum('ARRAY', 'COMPUTATION_RESULT')

init()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    arr = np.random.rand(array_size)

    print "arr size:", find_numpy_array_human_size(arr)

    track_time("1 process work time:", lambda : sum_els(arr))

    mp_s_time = current_time_millis()
    offset = int(array_size / size)
    self_arr = np.empty(1)

    for i in range(size):
        arr_i = np.empty(1)

        if i == size - 1:
            arr_i = arr[(i * offset):array_size]
        else:
            arr_i = arr[(i * offset):((i + 1) * offset)]

        if i == 0:
            self_arr = arr_i
        else:
            comm.ssend(arr_i, dest=i, tag=tags.ARRAY)

    all_sum = sum_els(self_arr)

    for i in range(1, size):
        all_sum = all_sum + comm.recv(source=i, tag=tags.COMPUTATION_RESULT)

    res = all_sum / array_size
    mp_f_time = current_time_millis()

    print size, "process work time:", (mp_f_time - mp_s_time), "millis"
else:
    arr = comm.recv(source=0, tag=tags.ARRAY)
    res = sum_els(arr)
    comm.send(res, dest=0, tag=tags.COMPUTATION_RESULT)

finalize()
