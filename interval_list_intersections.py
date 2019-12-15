class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        # ans = []
        # first = 0
        # second = 0
        # count = 0
        # while first < len(A) - 1
        #     while second < len(B) - 1:
        #         if second[0] <= first[1] and second[1] >= first[0]:
        #             ans.append([max(second[0], first[0]), min(second[1], first[1])])
        #             second += 1
        #         else:
        #             second = first
        #             if first != len(A) - 1:
        #                 first += 1
        #             # count += 1
        #             break
            
        #     first += 1
        #     if first <= len(A) - 1:
        #         second = 0
        
        ans = []
        
        i = j = 0
        import pdb; pdb.set_trace()
        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            
            if lo <= hi:
                ans.append([lo, hi])
            
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        
        return ans

abc =Solution()
A = [[0,2],[5,10],[13,23],[24,25]];  B = [[1,5],[8,12],[15,24],[25,26]]
# A, B = [[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]
print (abc.intervalIntersection(A,B))


