# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def print_list(self, head):
        current = head
        print "[",
        while current != None:
            print current.val,
            current = current.next
            if not current is None:
                print ",",
        print "]",

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr = head
        while curr:
            new_node = Node(curr.val, None, None)
            tmp = curr.next
            curr.next = new_node
            new_node.next = tmp
            curr = tmp

        prev = head
        while prev:
            curr = prev.next
            if prev.random:
                curr.random = prev.random.next
            prev = curr.next
            
        org_head = head
        new_head = head.next

        final_head = new_head
        
        while org_head and org_head.next and new_head and new_head.next:
            org_head.next = org_head.next.next
            new_head.next = new_head.next.next
            org_head = org_head.next
            new_head = new_head.next
        
        org_head.next = None
        new_head.next = None

        return final_head

node = Node(1, None, None)
node_2 = Node(2, None, None)

node.next = node_2
node.random = node_2
node_2.random = node_2

abc = Solution()
abc.copyRandomList(node)
