# def remove_dups(str):
    
#     temp = ''

#     if str[0] != str[1]:
#         temp += str[0]
    
#     i = 1

#     n = len(str) -1

#     while(i < n):
#         # import pdb; pdb.set_trace()
#         if(str[i-1] != str[i] and str[i] != str[i+1]):
#             temp += str[i]
#         i+=1
    
#     if(len(temp) == 0):
#         return temp
    
#     if (len(temp)!= n):
#         return remove_dups(temp)
    
#     return temp

# new_str = 'acaaabbbacdddd'

# print remove_dups(new_str)

def getsolution(x):
    
    print (x)
    if len(x)<2:
        return x
    n = len(x)-1
    temp = ''
        
    if x[0] != x[1]:
        temp += x[0]
    
    i = 1
    
    while(i<=n):
        if i == n:
            if x[i-1] != x[i]:
                temp += x[i]
        elif x[i-1] != x[i] and x[i] != x[i+1]:
            temp += x[i]
        i+=1
    
    if(len(temp) == 0):
        return temp
    
    if(len(temp)-1 != n):
        return getsolution(temp)
        
        
    return temp

t = int(input())
while(t !=0):
    # N = int(input())
    # x = list(map(int,input().strip(' ').split(' ')))
    x = str(input().strip(' '))
    solution = getsolution(x)
    print (solution)
    t = t-1
