class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        d = {}
        d[-1] = 1
        res = []
        for i in range(len(arr)):
			d[i] = d[i - 1] ^ arr[i]
        for q in queries:
			s = q[0]
			e = q[1]
    			res.append(d[e] ^ d[s - 1])
        return res

arr = [1,3,4,8]; queries = [[0,1],[1,2],[0,3],[3,3]]
abc = Solution()
print (abc.xorQueries(arr, queries))

        
