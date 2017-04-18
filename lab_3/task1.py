from mpi4py import MPI

import numpy as np

from sys import argv

from lab_3.task1_utils import multiply_arrs
from tools.mpi_helper import init, finalize


# noinspection PyShadowingNames
from tools.utils import current_time_millis, find_numpy_array_human_size, enum, track_time

array_size = int(argv[1])

init()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
tags = enum('ARRAY_0', 'ARRAY_1', 'COMPUTATION_RESULT')

if rank == 0:
    a = np.random.rand(array_size)
    b = np.random.rand(array_size)

    print "a size:", find_numpy_array_human_size(a)
    print "b sizetas:", find_numpy_array_human_size(b)

    track_time("1 process work time", lambda: multiply_arrs(a, b))

    mp_s_time = current_time_millis()
    offset = int(array_size / size)
    self_a_i = np.empty(1)
    self_b_i = np.empty(1)

    for i in range(size):
        a_i = np.empty(1)
        b_i = np.empty(1)

        if i == size - 1:
            a_i = a[(i * offset):array_size]
            b_i = b[(i * offset):array_size]
        else:
            a_i = a[(i * offset):((i + 1) * offset)]
            b_i = b[(i * offset):((i + 1) * offset)]

        if i == 0:
            self_a_i = a_i
            self_b_i = b_i
        else:
            comm.ssend(a_i, dest=i, tag=tags.ARRAY_0)
            comm.ssend(b_i, dest=i, tag=tags.ARRAY_1)

    self_r = np.multiply(self_a_i, self_b_i)
    results = [self_r]

    for i in range(1, size):
        r = comm.recv(source=i, tag=tags.COMPUTATION_RESULT)
        results.append(r)

    mp_result = np.concatenate(results, axis=0)
    mp_f_time = current_time_millis()

    print size, "process work time:", (mp_f_time - mp_s_time), "millis"
else:
    a = comm.recv(source=0, tag=tags.ARRAY_0)
    b = comm.recv(source=0, tag=tags.ARRAY_1)
    r = multiply_arrs(a, b)
    comm.send(r, dest=0, tag=tags.COMPUTATION_RESULT)

finalize()
