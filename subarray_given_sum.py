start = 0
end = 0
sum = 0
i = 0
answer = []

while(i<=n-1):
    if(sum == g_sum):
        answer = [start+1,end+1]
        print() answer
    if(sum > g_sum):
        sum = sum - x[start]
        start += 1
    else:
        sum += x[i]
        end = i
        i +=1

answer.append(-1)
return answer