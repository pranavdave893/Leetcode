class Solution:
    def __init__(self):
        self.dp = {}

    
    def isInterleave(self, s1: str, s2: str, s3: str, i=0, j=0, k=0) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
    

        if (i, j, k) in self.dp:
            return self.dp[(i, j, k)]
        
        
        if i >= len(s1) and j >= len(s2) and k >= len(s3):
            return True
        

        if i < len(s1) and j < len(s2) and k < len(s3) and s3[k] != s1[i] and s3[k] != s2[j]:
            dp[(i, j, k)] = False
            return False
        

        r1, r2 = False, False

        if i < len(s1) and k < len(s3) and s3[k] == s1[i]:
            r1 = self.isInterleave(s1, s2, s3, i+1, j, k+1)
        
        if j < len(s2) and k < len(s3) and s3[k] == s2[j]:
            r2 = self.isInterleave(s1, s2, s3, i, j+1, k+1)

        
        self.dp[(i,j,k)] = r1 or r2
        return self.dp[(i,j,k)]

abc = Solution()
print (abc.isInterleave("a", "b", "aba"))