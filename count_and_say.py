def _count_and_say(n):
    if n == 1:
        return '1'
    elif n == 2:
        return '11'
    else:
        say = ''
        temp = _count_and_say(n-1)
        count = 1
        
        for i in range(len(temp)):
            if i == len(temp)-1:
                say += str(count) + temp[i]
                continue
            if temp[i] != temp[i+1]:
                say += str(count) + temp[i]
                count = 1
            else:
                count +=1
        return say
    







