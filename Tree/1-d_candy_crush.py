from functools import lru_cache
from itertools import groupby

def candyCrush1D(S):
    stack = []

    for x in S:
        if not stack:
            stack.append((x, 1))
        
        elif stack[-1][0] == x:
            stack.append((x, stack[-1][1]+1))
        
        elif stack[-1][1] >= 3:
            temp = stack[-1][0]
            while stack and stack[-1][0] == temp:
                stack.pop()
            
            if stack and stack[-1][0] == x:
                stack.append((x, stack[-1][1]+1))
            else:
                stack.append((x, 1))
        
        else:
            stack.append((x, 1))
    
    if stack and stack[-1][1] >= 3:
        temp = stack[-1][0]

        while stack and stack[-1][0] == temp:
            stack.pop()
    
    temp = [x[0] for x in stack]
    return ''.join(temp)

print (candyCrush1D("deeedbbcccbdaa"))





    


# def f(s, l_rm = []):
#     ''' return l_rm, s 
#         l_rm - running list of all indexes already excised in 
#                prev iters, and add to indexes for the (3+)-mer 
#                removed in current call of the function
#         s - with [possibly] one (3+)-mer removed
#     '''
    
#     counter = 0
#     tally = ""
#     rm1, rm2 = None, None
    
#     for i in range(len(s)):
#         if (s[i] == tally) and (i not in l_rm):
#             counter += 1
#             if counter == 3:
#                 rm1 = i - 2
#         else:
#             if counter >= 3:
#                 rm2 = i
#                 break
#             else:
#                 tally = s[i]
#                 counter = 1 
#     if rm1 is None:
#         return l_rm, s
#     else:
#         l_rm.extend(list(range(rm1, rm2)))
#         return l_rm, (s[:rm1] + s[rm2:])


# def g(s, b_log=False):
#     '''recursive reduction with branching all possiblilites:
#          - add a level to `branches` for each time (3+)-mer is removed
#            from its previous level. 
#          - multiple items in each level of the branch represent dif
#            possibilities of removal
#          - l_rm keeps track of previous indexes removed for that 
#            {level, item}, so that `f()`can avoid repeating the same
#            removal.
#     '''
    
#     level = 0
#     branches = [[s]]
    
#     while(True):
        
#         branches.append([])

#         for s in branches[level]:
#             l_rm = []
#             for _ in range(len(s)):
#                 l_rm, s2 = f(s, l_rm)
#                 if s2 in branches[level+1] or s2 == s:
#                     continue
#                 branches[level+1].append(s2)
#                 if b_log: print(branches)
            
#         if len(branches[level+1]) == 0:
#             len_s = [len(c) for c in branches[level]]
#             ind = len_s.index(min(len_s))
#             return branches[level][ind]
        
#         level += 1

# print (g("baaabbbabbccccd"))