a = [1,3,5,8,5,2,4,6,0]
k = 100
sum_a = 0
i = 0
x = False
while i < len(a)-1:
    sum_a += a[i]
    if sum_a == k:
        x= True
    if sum_a > k:
        i+=1
print x
