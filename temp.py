def getsolution(x,n,g_sum):
    start = 0
    end = 0
    sum = 0
    i = 0
    answer = []
    
    while(not (i> n-1)):
        if(i==35):
            import pdb; pdb.set_trace()
        if(sum == g_sum):
            answer = [start+1,end+1]
            return answer
        if(sum > g_sum):
            sum = sum - x[start]
            start += 1
        else:
            # if i > (n-1):
            #     break
            sum += x[i]
            end = i
            i +=1
    
    answer.append(-1)
    return answer

# t = int(input())
# while(t !=0):
n,g_sum = input().split(' ')
n = int(n)
g_sum = int(g_sum)
x = list(map(int,input().strip(' ').split(' ')))
solution = getsolution(x,n,g_sum)
print (*solution)
# t = t-1