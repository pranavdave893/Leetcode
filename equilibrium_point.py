#code
def getSolution(x,n):
    i = 0
    j = n - 1
    
    if j == 0:
        return x[j]
    l_sum = x[i]
    r_sum = x[j]
    
    while(i != j and i <j):
        if(l_sum > r_sum):
            j -= 1
            r_sum += x[j]
        if(l_sum < r_sum):
            i += 1
            l_sum += x[i]
        try:
            if(l_sum == r_sum and i!=j):
                i += 1
                j -= 1
                if (i==j):
                    return i+1
                else:
                    l_sum += x[i]
                    r_sum += x[j]
        except:
            import pdb; pdb.set_trace()
    return -1

t = int(input())
while(t !=0):
    n = int(input())
    x = list(map(int,raw_input().strip(' ').split(' ')))
    solution = getSolution(x,n)
    print (solution)
    t = t-1