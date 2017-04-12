from mpi4py import MPI

from utils.mpi_helper import finalize
from utils.mpi_helper import init

init()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print "process rank:", rank, "size:", size

finalize()
