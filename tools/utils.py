import time
import sys
from mpi4py import MPI


def current_time_millis(): return int(round(time.time() * 1000))


# noinspection PyShadowingBuiltins
def find_numpy_array_human_size(obj):
    bytes = obj.nbytes

    if bytes < 1024:
        return str(bytes) + " Bytes"

    bytes = bytes / 1024

    if bytes < 1024:
        return str(bytes) + " Kb"

    bytes = bytes / 1024

    if bytes < 1024:
        return str(bytes) + " Mb"

    return str(bytes / 1024) + " Gb"


def enum(*sequential, **named):
    """Handy way to fake an enumerated type in Python
    http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
    """
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


def track_time(message, func):
    s_time = current_time_millis()
    func()
    f_time = current_time_millis()
    print message + ":", (f_time - s_time), "millis"


def format_human_time(millis):
    if millis == 0:
        return "0 millis"

    if millis < 1000:
        return str(millis) + " millis"

    seconds = millis / 1000
    millis = millis - (seconds * 1000)

    if seconds < 60:
        res = ""

        if seconds != 0:
            res = str(seconds) + " seconds"

        if millis != 0:
            res = res + ", " + format_human_time(millis)

        return res
    else:
        minutes = seconds / 60
        res = str(minutes) + " minutes"
        seconds = seconds - (minutes * 60)
        res = res + ", " + format_human_time((seconds * 100) + millis)

    return res


def smart_print(msg, rank=None):
    if not rank:
        comm = MPI.COMM_WORLD
        rank = comm.rank

    sys.stdout.write("[" + str(rank) + "] " + msg)

