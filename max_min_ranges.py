start = [1,1,1,3]
end = [14,8,3,7]
l = len(start)
n = max(end) + 2 

result = [0]*n

for i in start:
    result[i] += 1
for i in end:
    result[i+1] -=1

largest = result[0]
smallest = result[0]
for i in range(1,n):
    result[i] += result[i-1]
    if result[i] >= largest:
        import pdb; pdb.set_trace()
        largest = i
    if result[i] > smallest:
        smallest = i

print result
print largest+1,smallest