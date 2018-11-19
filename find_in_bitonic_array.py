x = [-3,9,8,20,17,5,1,0]
low = 0
high = len(x)-1
key = 5

def findpivot(x,low,high):

    mid = int((low+high)/2)

    if x[mid] > x[mid+1] and x[mid] > x[mid-1]:
        return mid
    
    if x[mid] < x[mid+1]:
        return findpivot(x,mid,high)
    
    return findpivot(x,low,mid)

def binarySearch(x,low,high,key):

    mid = int((low+high)/2)

    if mid == key:
        return mid

    if x[mid]>key:
        return binarySearch(x,low,mid,key)
    
    if x[mid]<key:
        return binarySearch(x,mid,high,key)

pivot = findpivot(x,low,high)

first = binarySearch(x,0,pivot,key)

if first != -1:
    print first
else:
    print binarySearch(x,pivot,high,key)



