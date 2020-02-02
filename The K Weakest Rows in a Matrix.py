from collections import Counter
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        ans = []
        for i, x in enumerate(mat):
            count = Counter(mat[i])
            ans.append((count[1], i))
        
        ans.sort(key=lambda x :x[0])

        new_ans = [x[1] for x in ans]
        return new_ans[:k]

abc = Solution()
abc.kWeakestRows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 2)
        

