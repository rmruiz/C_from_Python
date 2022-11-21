from ctypes import *
so_file = "/Users/rolando.ruiz/git/C_from_Python/my_functions.so"
my_functions = CDLL(so_file)

#print(type(my_functions))
#print(my_functions.square(10))
#print(my_functions.square(8))

def square(i):
    j = 0
    for x in range(i):
        j += 1*2*3*4*5*6*7*8*9*10
    return 8

import timeit
from functools import partial

if __name__ == '__main__':

    input = 100
    iterations = 100000

    c_code = min(timeit.repeat(partial(my_functions.square, input), number=iterations))
    py_code = min(timeit.repeat(partial(square, input), number=iterations))
    print(f"c_code:{c_code}")
    print(f"py_code:{py_code}")
    print(f"Perf Improvement: {(py_code-c_code)/py_code:.2%}")