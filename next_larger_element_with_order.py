# '''
# https://practice.geeksforgeeks.org/problems/next-larger-element/0
# '''

# x = [8,7,3,2,4,9,5,4,6]
# i = len(x)-1
# stack = []
# ans = [None] * len(x)
# def isempty(st):
#     if len(st) == 0:
#         return True
#     else:
#         return False

# while(i>=0):
    
#     if not isempty(stack):
#         top = stack[-1]
#         prev = x[i]
#         while(len(stack) > 0 and top<=prev):
#             stack.pop()
#             if(isempty(stack)):
#                 break
#             top = stack[-1]

        
#     if(isempty(stack)):
#         ans[i] = -1
#     else:
#         ans[i] = stack[-1]
#     stack.append(x[i])
    
#     i -= 1

# print (ans)

def isempty(s):
    if len(s) == 0:
        return True
    else:
        return False

def getsolution(x):
    i = len(x)-1
    stack = []
    solution = [None]*len(x)
    while(i>=0):
        if not len(stack) == 0:
            top = stack[-1]
            prev = x[i]
            while(len(stack)>0 and top<=prev):
                stack.pop()
                if len(stack) == 0:
                    break 
                top = stack[-1]
        
        if len(stack) == 0:
            solution[i] = -1
        else:
            solution[i] = stack[-1]
        stack.append(x[i])
        i -= 1
    return solution
    
#     return solution


t = int(input())
while(t !=0):
    N = int(input())
    x = list(map(int,input().strip(' ').split(' ')))
    solution = getsolution(x)
    print (*solution)
    t = t-1

