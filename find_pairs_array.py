a = [1,2,4,5,7]
b = [5,6,3,4,8]

key = 9

sum_map = {}

for i in b:
    sum_map[i] = i

for i in a:
    if (key-i) in sum_map.values():
        print (i,(key-i))

