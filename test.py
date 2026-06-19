from ctypes import *
so_file = "/Users/rolando/git/C_from_Python/my_functions.so"
my_functions = CDLL(so_file)

#int cpu_intensive(int i) {
#	double j = 0.0;
#	for(int x=1;x<i;x++){
#		j += i;
#		j *= 1.0000001;
#		j /= 1.0000001;
#	}
#	return j;
#}


def cpu_intensive(i):
  j = 0.0
  for x in range(i):
    j = j + i
    j = j * 1.0000001
    j = j / 1.0000001
  return j

import timeit
from functools import partial

if __name__ == '__main__':

    input = 100
    iterations = 100000

    c_code = min(timeit.repeat(partial(my_functions.cpu_intensive, input), number=iterations))
    py_code = min(timeit.repeat(partial(cpu_intensive, input), number=iterations))
    print(f"c_code:{c_code}")
    print(f"py_code:{py_code}")
    print(f"Perf Improvement: {(py_code-c_code)/py_code:.2%}")
