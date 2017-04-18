import os
# import tools.tools as util
from utils import current_time_millis, format_human_time


def run_mpi_script(script_path, process_count, params=None):
    script_path = str(script_path)

    if process_count > 1:
        process_count = str(process_count)
        print "run script: " + script_path + ", process count:" + process_count, ", params:", params
        s_time = current_time_millis()
        if params:
            os.system("mpirun -np " + process_count + " python " + script_path + " " + str(params))
        else:
            os.system("mpirun -np " + process_count + " python " + script_path)
        f_time = current_time_millis()
        print "EXECUTION TIME:", format_human_time(f_time - s_time)
    else:
        raise ValueError("process count must be > 1!")
