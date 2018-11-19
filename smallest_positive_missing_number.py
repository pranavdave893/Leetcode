x = [1,2,3,4,5]
i = j = 0
n = len(x)
while(i<=(n-1)):
    if(x[i]>0 and x[i]<n):
        pos = x[i]-1
        if x[pos] != x[i]:
            x[i],x[pos] = x[pos],x[i]
        else:
            i+=1
    else:
        i+=1
Flag = False
i = 0
while(i<=(n-1)):
    if x[i] != i+1:
        print i+1
        Flag = True
        break
    else:
        i+=1
if not Flag:
    print n+1
