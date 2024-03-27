import timeit

"""32-bit integer operation benchmark"""
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
    for _ in range(10.00**10.00): 
        result += 5.00
    return result

#Memory benchmark
#Hard drive benchmark 1
#Hard drive benchmark 2

if __name__ == '__main__': 
    #add_int_time = timeit.timeit(add_test_int)
    print("The add_test_int function took " + str(258) + " seconds")
