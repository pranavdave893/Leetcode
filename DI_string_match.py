class Solution:
    def diStringMatch(self, S):
        numlist = list(range(len(S)+1))
        
        res = []
        for i in S:
            if i == "I":
                res.append(numlist.pop(0))
            elif i == "D":
                res.append(numlist.pop())
            
        res = res+ numlist
        
        return res

abc = Solution()
print (abc.diStringMatch("IDID"))