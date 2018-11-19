x = [4,1,2,-1]

j = len(x)-1
max_so_far = -1
while j>=0:
    temp = x[j]

    # Inter change 9 and 10 for largest element including it self
    x[j] = max_so_far
    max_so_far = max(max_so_far,temp)
    j = j-1
print x