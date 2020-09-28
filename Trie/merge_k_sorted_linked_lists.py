"""
https://leetcode.com/problems/merge-k-sorted-lists/
"""
from heapq import heappush, heappop
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        dummy = ListNode(val=None)
        
        curr = dummy
        
        heap = []
        
        for node in lists:
            if node and node.val != None:
                heappush(heap, (node.val, node))
        
        while heap:
            nxt_val, node = heappop(heap)
            curr.next = node
            curr = curr.next
            if curr.next:            
                heappush(heap, (curr.next.val, curr.next))
            
        return dummy.next