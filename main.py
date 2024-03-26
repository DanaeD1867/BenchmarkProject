import timeit
#32-bit integer operation benchmark

#10^10 additions
def add_test_int(): 
    result = 0 
    for _ in range(10**10): 
        result += 5
    return result

#10^9 mulitplication
def mult_test_int(): 
    result = 1
    for _ in range(5*10**9): 
        result *= 2
    return result

if __name__ == '__main__': 
    add_int_time = timeit.timeit(add_test_int)
    print(add_int_time)

#64-bit floating point operation benchmark
#Memory benchmark
#Hard drive benchmark 1
#Hard drive benchmark 2
