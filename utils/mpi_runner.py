import os


def run_mpi_script(script_path, process_count, params=None):
    script_path = str(script_path)

    if process_count > 1:
        process_count = str(process_count)
        print "run script: " + script_path + ", process count:" + process_count, ", params:", params

        if params:
            os.system("mpirun -np " + process_count + " python " + script_path + " " + str(params))
        else:
            os.system("mpirun -np " + process_count + " python " + script_path)
    else:
        raise ValueError("process count must be > 1!")
