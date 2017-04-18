from tools.mpi_runner import run_mpi_script

print "TASK 1 -------------------------"
run_mpi_script("task1.py", process_count=8, params=10 * 1000 * 1000)

print "TASK 2 -------------------------"
run_mpi_script("task2.py", process_count=8, params=10 * 1000 * 1000)

print "TASK 3 -------------------------"
run_mpi_script("task3.py", process_count=8, params=10 * 1000 * 1000)

print "TASK 4 -------------------------"
run_mpi_script("task4.py", process_count=8, params=10 * 1000 * 1000)
