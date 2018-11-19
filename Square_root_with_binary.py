if (x == 0 or x == 1):
    return x
start = 1
end = x/2
while(start<=end):
    mid = (start+end)//2
    
    if (mid == x/mid):
        return mid
    elif(mid < x/mid):
        ans = mid
        start = mid+1
    else:
        end = mid-1
return ans