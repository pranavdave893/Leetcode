#code
from __future__ import print_function
T = int(input(""))
if T < 1 or T > 100:
    raise ValueError
for i in range(T):
    N = int(input(""))
    
    if N < 1 or N > 500:
        break
        
    ip = (input())
        
    # if ip < 1 or ip > 1000:
    #     break

    arr = list(map(int, ip.strip(' ').split(' ')))

    for i in range(len(arr)):
        if i == len(arr)-1:
            print (-1)
        elif arr[i+1] < arr[i]:
            print (arr[i+1], end=" ")
        else:
            print (-1,end=" ")