/* 
"""
https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0
https://coderbyte.com/algorithm/dutch-national-flag-sorting-problem
https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

Example:

Input :

2
5
0 2 1 2 0
3
0 1 0
 
Output:

0 0 1 2 2
0 0 1
"""
def sortarray(x):
    low = 0
    mid = 0
    high  = len(x)-1
    while(mid <= high):
        if (x[mid] == 0):
            x[mid],x[low] = x[low],x[mid]
            low += 1
            mid += 1
        elif (x[mid] == 2):
            x[mid],x[high] = x[high],x[mid]
            high -= 1
        elif (x[mid] == 1):
            mid +=1
    
    return x

t = int(input())
while(t !=0):
    n = int(input())
    x = list(map(int,input().strip(' ').split(' ')))
    print (*sortarray(x))
    t = t-1

