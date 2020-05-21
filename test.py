def fibonacciSimpleSum(n):

    fib_array = [0, 1]
    
    i = 0
    j = 1

    while fib_array[-1] < n:
        fib_array.append(fib_array[i] + fib_array[j])
        i += 1
        j += 1

    fib_array = set(fib_array)

    for x in fib_array:
        if n-x in fib_array: return True
    
    return False

print (fibonacciSimpleSum(66))