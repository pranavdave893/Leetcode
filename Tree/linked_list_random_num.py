from __future__ import annotation
import random

"""
Q : https://leetcode.com/problems/linked-list-random-node/
A: https://leetcode.com/problems/linked-list-random-node/, 
A2: https://leetcode.com/problems/linked-list-random-node/discuss/297969/Python-Beats-90-Never-Using-Length
"""
class Solution(object):
    def __init__(self, head: ListNode):
        self.head = head
    
    
    def getRandom(self) -> int:
        result, node, index = self.head, self.head.next, 1

        while node:
            if random.ranint(0, index) == 0:
                result = node
            node = node.next
            index += 1
        return result.val



