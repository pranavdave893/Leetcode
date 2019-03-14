class Solution:
    def flipAndInvertImage(self, A):
        i = 0
        while i <= len(A)-1:
            A[i] = A[i][::-1]
            j = 0 
            while j <= len(A[i])-1:
                # import pdb; pdb.set_trace()
                A[i][j] = 1 if A[i][j] == 0 else 0
                j += 1
            i += 1
        return A

abc = Solution()
print (abc.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
