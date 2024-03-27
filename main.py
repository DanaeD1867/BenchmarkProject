import timeit
import numpy as np

"""32-bit integer operation benchmark"""
#10^10 additions
def add_test_int(): 
    result = 0 
    for _ in range(10**10): 
        result += 2
    return result

#10^9 mulitplication
def mult_test_int(): 
    result = 1
    for _ in range(5*10**9): 
        result *= 2
    return result

#2*10^9 division
def division_test_int(): 
    result = 5**10
    for _ in range(2 * 10**9): 
        result /= 2
    return result


"""64-bit floating point operation benchmark"""
#10^10 additions
def add_test_float(): 
    result = 0.00
    for _ in range(10**10): 
        result += 5.00
    return result

#10^9 mulitplication
def mult_test_float(): 
    result = 1.00
    for _ in range(5*10**9): 
        result *= 2.00
    return result

#2*10^9 division
def division_test_float(): 
    result = 5.00**10.00
    for _ in range(2.00 * 10.00**9.00): 
        result /= 2.00
    return result

#Memory benchmark
def read_array_test(): 
    lst = np.zeros(5*10**9, dtype=np.int32)
    result = 0
    for i in range(5 * 10**9): 
        result += lst[i]
    return result

def write_array_test(): 
    lst = np.zeros(5*10**9, dtype=np.int32)
    for i in range(5*10**9): 
        lst[i] = i
    return lst

#Hard drive benchmark 1
def drive_test_read_1(): 
    pass
    
def drive_test_write_1(): 
    pass

#Hard drive benchmark 2
def drive_test_write_2(): 
    pass

def drive_test_read_2(): 
    pass

if __name__ == '__main__': 
    #add_int_time = timeit.timeit(add_test_int)
    #print("The add_test_int function took " + str(add_int_time) + " seconds")

    #mult_int_time = timeit.timeit(mult_test_int)
    #print("The mult_test_int function took " + str(mult_int_time) + " seconds")

    #divide_int_time = timeit.timeit(division_test_int)
    #print("The divide_test_int function took " + str(divide_int_time) + " seconds")

    #add_float_time = timeit.timeit(add_test_float)
    #print("The add_test_float function took " + str(add_float_time) + " seconds") 

    
    mult_float_time = timeit.timeit(mult_test_float)
    print("The mult_test_int function took " + str(mult_float_time) + " seconds")

    #read_array_time = timeit.timeit(read_array_test)
    #print('The read_array_test function took ' + str(read_array_time) + ' seconds')

    #write_array_time = timeit.timeit(write_array_test)
    #print('The read_array_test function took ' + str(write_array_time) + ' seconds')
    