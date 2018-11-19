def getsolution(x,N):

    count_map = {}
    answer = []
    for i in x:
        if count_map[abs(i)] == 0:
            count_map[abs(i)] = 1
        else:
            answer.append(abs(i))
        
    
        
    return answer

t = int(input())
while(t !=0):
    N = int(input())
    x = list(map(int,input().strip(' ').split(' ')))
    solution = getsolution(x,N)
    print (*solution)
    t = t-1