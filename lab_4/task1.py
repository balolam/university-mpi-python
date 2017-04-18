from mpi4py import MPI
from tools.utils import smart_print

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    data = {'magic_value': 42}
    smart_print("Hi, Parallel Programmer!\n")
    smart_print("send: " + str(data) + '\n')
    comm.bcast(data, root=0)
else:
    data = comm.bcast(None, root=0)
    smart_print("received: " + str(data) + '\n')




