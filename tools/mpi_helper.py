from mpi4py import MPI


def init():
    if not MPI.Is_initialized():
        # print "initializing..."
        MPI.Init()
    else:
        pass
        # print "initiated before!"


def finalize():
    if not MPI.Is_finalized():
        # print "finalizing..."
        MPI.Finalize()
    else:
        pass
        # print "finalized before!"
