class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        digit = []
        stack = []
        temp = []
        for x in s:
            
            if x.isdigit():
                digit.append(x)
                continue
            elif digit:
                number = int("".join(digit))
                stack.append(str(number))
                digit = []
                
            if x == "[":
                continue
            if x == "]":
                temp = []
                while stack and not stack[-1].isdigit():
                    temp.append(stack.pop())
                number = int(stack.pop())
                temp = temp * number
                for x in temp[::-1]:
                    stack.append(x)
                temp = []
            else:
                stack.append(x)
        
        while stack:
            temp.append(stack.pop())

        return ''.join(temp[::-1])

abc = Solution()
print (abc.decodeString("3[a]2[bc]"))
# print (abc.decodeString("3[a2[c]]"))
# print (abc.decodeString("2[abc]3[cd]ef"))
# print (abc.decodeString("3[2[a]2[2[b]c]]"))
# print (abc.decodeString("100[leet]"))
            
            
            

