a = [-2,1,-3,4,-1,2,1,-5,4]

sum = 0
max_sum = 0
start = 0
k = 6
for i in range(len(a)-1):
    sum +=a[i]
    if sum > max_sum:
        max_sum = sum
        end = i
        start = s
    if sum<0: 
        sum = 0
        s = i+1
        
print max_sum
print start,end
print a[start:end+1]