from mpi4py import MPI


def init():
    if not MPI.Is_initialized():
        # print "initializing..."
        MPI.Init()
    # else:
    #     print "initiated before!"


def finalize():
    if not MPI.Is_finalized():
        # print "finalizing..."
        MPI.Finalize()
    # else:
    #     print "finalized before!"
