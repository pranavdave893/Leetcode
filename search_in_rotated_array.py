"""
https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array/0

"""
def binarySearch(x,low,high,key):
    if high < low:
        return -1
    mid = int((low+high)/2)
    
    if x[mid] == key:
        return mid
    
    if key > x[mid]:
        return binarySearch(x,mid+1,high,key)
    
    return binarySearch(x,low,mid-1,key)

def findpivot(x,low,high):
    if high < low:
        return -1
    if high == low:
        return low
    
    mid = int((low+high)/2)
    
    if mid<high and x[mid] > x[mid+1]:
        return mid
    if mid > low and x[mid] < x[mid-1]:
        return mid-1
    if x[0] >= x[mid]:
        return findpivot(x,0,mid-1)
    return findpivot(x,mid+1,high)


def getsolution(x,N,key):
    
    pivot = findpivot(x,0,N)
    
    if pivot == -1:
        return binarySearch(x,0,N,key)
        
    if x[pivot] == key:
        return pivot
    
    if x[0]<=key:
        return binarySearch(x,0,pivot,key)
    return binarySearch(x,pivot+1,N,key)
    
    # return answer

t = int(input())
while(t !=0):
    N = int(input())
    x = list(map(int,input().strip(' ').split(' ')))
    key = int(input())
    solution = getsolution(x,N-1,key)
    print (solution)
    t = t-1