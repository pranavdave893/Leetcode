class Solution(object):
    def __init__(self):
        self.ans = []
    
    def sum_100(self, s, ans, path=""):
        if len(s) == 0 or ans == 100:
            self.ans.append(path)
        
        for i in range(len(s)):
            self.sum_100(s[i+1:], ans - int(s[:i+1]), path + "+" + s[:i+1])
            self.sum_100(s[i+1:], ans - int(s[:i+1]), path + "-" + s[:i+1])

a = Solution()
a.sum_100("123456789", 0)
for i in a.ans:
    print (i)



