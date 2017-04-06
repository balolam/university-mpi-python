from mpi4py import MPI

from mpi_utils import finalize
from mpi_utils import init

init()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print "process rank:", rank, "size:", size

finalize()
