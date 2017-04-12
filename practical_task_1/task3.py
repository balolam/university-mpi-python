from mpi4py import MPI

from utils.mpi_helper import finalize
from utils.mpi_helper import init

init()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print "process [", rank, "] - running"

if rank % 2 == 0:
    data = {'name': "PROCESS-" + str(rank), 'msg': "Hello"}
    req = comm.isend(data, dest=rank + 1, tag=0)
    req.wait()
else:
    req = comm.irecv(source=rank - 1, tag=0)
    data = req.wait()
    print "process-" + str(rank) + ":", data['name'], "say", data['msg']

finalize()
