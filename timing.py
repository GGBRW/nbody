import os 
import sys
from time import perf_counter


def time_both(n):
    time_python(n)
    time_cpp(n)


def time_python(n):
    t_start = perf_counter()
    os.system(f"python ./nbody.py {n}")
    t_stop = perf_counter()
    print(f"Running time python program: {(t_stop - t_start)} sec")

def time_cpp(n):
    t_start = perf_counter()
    os.system(f"./nbody {n}")
    t_stop = perf_counter()
    print(f"Running time C++ program: {(t_stop - t_start)} sec")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])
        if len(sys.argv) > 2 and sys.argv[2] == "python":
            time_python(n)
        elif len(sys.argv) > 2 and (sys.argv[2] == "c++" or sys.argv[2] == "cpp"):
            time_cpp(n)
        elif len(sys.argv) > 2 and sys.argv[2] == "pythonall":
            for i in [5000,500000,5000000,50000000]:
                time_python(i)
        else:
            time_both(n)
