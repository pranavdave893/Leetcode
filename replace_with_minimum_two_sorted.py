x = [3,-1,5,-1,8,-1,12]
b = [2,7,10]

j = len(x)-1
k = j

while(j>=0):
    if x[j]<0:
        j = j-1
    if j < 0 :
        break
    if (x[j] > 0 and x[k]<0):
        x[j],x[k] = x[k],x[j]
        k = k-1
    else:
        j = j-1
        if not x[k]<0:
            k = k-1

print x
for i in range(len(x)-1):
    if x[i]>0:
        j = i
        break
i=0
k=0
while i<=len(b)-1:
    if b[i] < x[j]:
        x[k] = b[i]
        k += 1
        i += 1
    if i >= len(b):
        break
    if x[j] < b[i]:
        x[k] = x[j]
        j += 1
        k += 1
print x
