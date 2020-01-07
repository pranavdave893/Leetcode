#https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/327757/Python-merge-sort-clear-explanation-and-think-process
# TODO : https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76639/Python-solutions-with-detailed-explanation
class Solution:
    def countSmaller(self, nums):

        def mergeLists(arr1, arr2):
            res=[]
            idx1, idx2, addCnt=0,0,0

            while idx1<len(arr1) or idx2<len(arr2):
                v1=arr1[idx1][0] if idx1<len(arr1) else float('inf')
                v2=arr2[idx2][0] if idx2<len(arr2) else float('inf')

                if v1<=v2:
                    res.append(arr1[idx1])
                    arr1[idx1][1]+=addCnt
                    idx1+=1
                else:
                    res.append(arr2[idx2])
                    idx2+=1
                    addCnt+=1
            return res

        def sortList(list1):
            n=len(list1)
            if n<=1:
                return list1
            a=sortList(list1[:n//2])
            b=sortList(list1[n//2:])
            return mergeLists(a,b)

        tmpList = [[n,0,i] for i,n in enumerate(nums)]
        tmpList2=sortList(tmpList)
        res=[0]*len(nums)

        for t in tmpList2:
            res[t[2]]=t[1]
        return res
    

abc = Solution()
abc.countSmaller([2,3,0,-4,2,5,0,-1,-2])

from heapq import heappush, heappop
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def mergeList(list1, list2):
            res = []            
            idx1, idx2, add_count = 0, 0, 0
            
            while idx1 < len(list1) or idx2 < len(list2):
                v1 = list1[idx1][0] if idx1 < len(list1) else float('inf')
                v2 = list2[idx2][0] if idx2 < len(list2) else float('inf')
                
                if v1 <= v2:
                    res.append(list1[idx1])
                    list1[idx1][1]+=add_count
                    idx1 += 1
                else:
                    res.append(list2[idx2])
                    idx2 += 1
                    add_count += 1
            return res
 
        def sortList(list1):
            n = len(list1)
            if n <= 1:
                return list1
            a = sortList(list1[:n//2])
            b = sortList(list1[n//2:])
            return mergeList(a, b)
            
        tmplist = [[n,0,i] for i,n in enumerate(nums)]
        tmplist2 = sortList(tmplist)
        res = [0]*len(nums)
        
        
        for i in tmplist2:
            res[i[2]] = i[1]
        
        return res