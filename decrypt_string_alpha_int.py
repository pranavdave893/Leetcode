import string
from collections import deque
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        dct = {}
        count = 1

        for x in string.ascii_lowercase:
            dct[str(count)] = x
            count += 1
        
        dq = deque()
        ans = []
        x = len(s)-1
        stack = []

        while x >=0:
            tmp = ""
            if s[x] == "#":
                while dq:
                    ans.append(dct.get(dq.popleft(), ''))
                ct = 0
                while ct < 2:
                    x -= 1
                    stack.append(s[x])
                    ct += 1
                
                while stack:
                    tmp += stack.pop()
                
                ans.append(dct.get(tmp, ''))
            
            else:
                dq.append(s[x])
            
            x -= 1
        
        while dq:
            ans.append(dct.get(dq.popleft(), ''))
        
        return ''.join(ans[::-1])

abc = Solution()
print (abc.freqAlphabets("10#11#12"))
print (abc.freqAlphabets("1326#"))
print (abc.freqAlphabets("25#"))
print (abc.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
        







