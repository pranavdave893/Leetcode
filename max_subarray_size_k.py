
def getsolution(x,n,k):
    solution = []
    c = 0
    max_num = []
    while(k != len(x)+1):
        max_num.append(max(x[c:k]))
        c += 1
        k += 1
    return max_num

for _ in range(int(input())):
    n,k = map(int,input().strip(' ').split(' '))
    x = list(map(int,input().strip(' ').split(' ')))
    solution = getsolution(x,n,k)
    print (*solution)