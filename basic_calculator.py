"""
https://leetcode.com/problems/basic-calculator/
tags: Math, Stack, Hard, Houzz, 
"""
class Solution():
    
    def calculate(self, s):
        def update(op, v):
            if op == "+": stack.append(v)
            elif op == "-": stack.append(-v)
            elif op == "*": stack.append(stack.pop() * v)
            elif op == '/': 
                prev_val = stack.pop()
                if prev_val < 0:
                    prev_val = -prev_val
                    stack.append(-(int(prev_val//v)))
                else:
                    stack.append(int(prev_val//v))
        

        pt, num, stack, sign = 0, 0, [], "+"

        while pt < len(s):
            if s[pt].isdigit():
                num = num * 10 + int(s[pt])
            
            elif s[pt] in "+-*/":
                update(sign, num)
                num, sign = 0, s[pt]
            
            elif s[pt] in "(":
                num, j = self.calculate(s[pt+1:])
                pt = pt + j
            
            elif s[pt] in ")":
                update(sign, num)
                return sum(stack), pt + 1
            
            pt += 1

        update(sign, num)
        return sum(stack)

abc = Solution()
# print (abc.calculate("2+3-5+10+(10+15)"))
print (abc.calculate("14-3/2"))