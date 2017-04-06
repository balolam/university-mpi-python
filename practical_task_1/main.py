import os
import sys

print "TASK 1 -------------------------"
os.system("mpirun -np 2 python task1.py")
print "TASK 2 -------------------------"
os.system("mpirun -np 2 python task2.py")
print "TASK 3 -------------------------"

argv = sys.argv
size = int(sys.argv[1])

if not size:
    raise ValueError("size does not exists!")

if size % 2 != 0:
    raise ValueError("size % 2 != 0!")

os.system("mpirun -np " + str(size) + " python task3.py")
