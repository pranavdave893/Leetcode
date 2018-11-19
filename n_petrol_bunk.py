t = int(input())
n = int(input)
while(t !=0):
    x = list(map(int,input().strip(' ').split(' ')))
    f = []
    d = []
    j = 1
    i = 0
    while (j<len(x)-1 or i < len(x)-1):
        f.append(x[i])
        i = i + 2
        d.append(x[j])
        j = j + 2

    i= 0
    min_fuel = 1
    last = 0
    while(i<len(f)):
        last += f[i]
        last -= d[i]
        i += 1
        if(last < min_fuel):
            min_fuel = last
            pos = i+1

    if last >=0:
        print (pos)
    else:
        print (-1)

    t -= 1





