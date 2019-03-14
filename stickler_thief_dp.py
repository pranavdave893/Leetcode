"""
Dynamic Programming, Array
Probelm Link : https://practice.geeksforgeeks.org/problems/stickler-theif/0
Solution : https://www.geeksforgeeks.org/find-maximum-possible-stolen-value-houses/

"""

def getsolution(x,n):
    
    if n == 0:
        return 0
    if n == 1:
        return x[0]
    if n == 2:
        return max(x[0],x[1])

    dp = [0]*n

    dp[0] = x[0]
    dp[1] = max(x[0],x[1])
    
    for i in range(2,n):
        dp[i] = max(x[i] + dp[i-2],dp[i-1])

    return dp[-1]

t = int(input())
while(t !=0):
    n = int(input())
    x = list(map(int,input().strip(' ').split(' ')))
    solution = getsolution(x,n)
    print (solution)
    t = t-1