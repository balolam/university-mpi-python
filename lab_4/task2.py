from mpi4py import MPI
from tools.utils import smart_print

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    f1 = float(raw_input('Input[float] 1: '))
    f2 = float(raw_input('Input[float] 2: '))
    i = int(raw_input('Input[int] 2: '))
    data = {'f1': f1, 'f2': f2, 'i': i}
    smart_print("Hi, Parallel Programmer!\n")
    smart_print("send:" + str(data) + '\n')
    comm.bcast(data, root=0)
else:
    data = comm.bcast(None, root=0)
    smart_print("process got: " + str(data) + '\n')




