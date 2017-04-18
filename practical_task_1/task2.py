from mpi4py import MPI

from tools.mpi_helper import finalize
from tools.mpi_helper import init

init()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print "process [", rank, "] - running"

if rank == 0:
    data = {'name': "PROCESS-" + str(rank), 'msg': "Hello"}
    req = comm.isend(data, dest=1, tag=11)
    req.wait()
elif rank == 1:
    req = comm.irecv(source=0, tag=11)
    data = req.wait()
    print "process-" + str(rank) + " receive:", data['name'], "say", data['msg']

finalize()
