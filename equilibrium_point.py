#code
t = int(input())
while (t !=0):
    _ = int(input())
    x = list(map(int,input().strip(' ').split(' ')))
    i = 0
    j = len(x) - 1
    
    if j == 1:
        print (-1)
        break
    l_sum = x[i]
    r_sum = x[j]
    
    while(i != j or j<i or i>j):
        if(l_sum > r_sum):
            j -= 1
            r_sum += x[j]
        
        if(l_sum < r_sum):
            i += 1
            l_sum += x[i]
        
        if(l_sum == r_sum and i!=j):
            i += 1
            j -= 1
            if (i==j):
                print (i)
                break
            else:
                l_sum += x[i]
                r_sum += x[j]
    print (-1)
    t = t-1