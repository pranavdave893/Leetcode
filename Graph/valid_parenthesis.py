class Solution:
    def checkValidString(self, s):
        s = list(s)
        abcd = "abcdefghijklmnopqrstuvwxyz"
        num = [i for i in range(10)]
        
        abc = []
        nm = []
        ans = []
        for x in range(len(s)):
            if s[x] in abcd:
                abc.append(s[x])
            else:
                nm.append(s[x])
        
        if abs(len(abc)-len(nm)) >= 2:
            return ""
        
        st = 0
        n = 0
        
        while st < len(abc) and n < len(nm):
            ans.append(abc[st])
            ans.append(nm[n])
            
            st += 1
            n += 1
        
        if st < len(abc):
            for x in abc[st:]:
                ans.append(x)
        
        if n < len(nm):
            for x in nm[n:]:
                ans.append(x)
        
        return "".join(ans)



abc = Solution()
print (abc.checkValidString("covid2019"))