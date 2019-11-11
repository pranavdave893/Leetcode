from heapq import heappush, heappop
class Solution(object):
    def minMeetingRooms(self, intervals):

        intervals.sort(key = lambda x:x[0])
        heap = []
        for it in intervals:
            if heap and heap[0] <= it[0]:
                heappop(heap)
            heappush(heap, it[1])
        
        return len(heap)

    def minMeetingRooms_start_end(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        start = []
        end = []

        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        
        start.sort()
        end.sort()

        s = e = 0
        answer = available = 0

        while s<len(start):
            if start[s] < end[e]:
                if available == 0:
                    answer += 1
                else:
                    available -= 1
                
                s+=1
            else:
                available += 1
                e+= 1
        
        return answer
        
        # Python Stupid solution which solves 69 test cases out of 78 on LC as of 11/3/19.
        # if not intervals:
        #     return 0
        
        # ans = 1
        # intervals.sort()
        # first = intervals[0]
        # min_end = float('inf')
        
        # for i in intervals[1:]:
        #     if (first[0] <= i[0] <= first[1]):
        #         if min_end and i[0] >= min_end:
        #             min_end = min(i[1], first[1])
        #             first = i
        #             continue
        #         elif i[0] == first[1] and not (i[1] <= first[1]):
        #             first = i
        #             continue
        #         else:
        #             ans += 1
        #             min_end = min(i[1], first[1], min_end)
        #     first = i

        # return ans

abc = Solution()
print (abc.minMeetingRooms([[0,30],[5,10],[15,20]])) #2
print (abc.minMeetingRooms([[9,10],[4,9],[4,17]]))  # 2 
print (abc.minMeetingRooms([[7,10],[2,4]])) #1
print (abc.minMeetingRooms([[13,15],[1,13]])) #1
print (abc.minMeetingRooms([[4,9],[9,17],[9,17]])) # 2
print (abc.minMeetingRooms([[1,5],[8,9],[8,9]])) #2
print (abc.minMeetingRooms([[8,14],[12,13],[6,13],[1,9]])) #3
print (abc.minMeetingRooms([[1,8],[6,20],[9,16],[13,17]])) #3
print (abc.minMeetingRooms([[2,36],[3,4],[13,34],[16,20],[39,46]])) #3