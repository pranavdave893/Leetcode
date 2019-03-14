from linked_list import Node

l1 = Node()
l1.insert_at_beginning(7)
l1.insert_at_end(2)
l1.insert_at_end(4)
l1.insert_at_end(3)
# l1.insert_at_end(5)

l2= Node()
l2.insert_at_beginning(5)
l2.insert_at_end(6)
l2.insert_at_end(4)



class ListNode(object):
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        
        first = l1
        second = l2
        
        import pdb; pdb.set_trace()
        carry = 0
        
        node = ListNode(None)
        head = node
        
        while first and second:
            l_sum = first.data + second.data + carry
            carry = 0
            if l_sum >= 10:
                carry = l_sum // 10
                l_sum = l_sum % 10
            
            new_node = ListNode(l_sum)
            node.next = new_node
            node = node.next
            
            first = first.next
            second = second.next
        
        import pdb; pdb.set_trace()

        if first:
            node.next = ListNode(first.data + carry)
            node = node.next
        if second:
            node.next = ListNode(second.next + carry)
            node = node.next
        if carry:
            carry_node = ListNode(carry)
            node.next = carry_node
            node = node.next
        
        head = head.next
        return_list = self.reverse(head)
        import pdb; pdb.set_trace()
        return return_list
    
    def reverse(self, head):
        prev = None
        curr = head
        if not curr or not curr.next:
            return head
        
        while curr:
            
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

abc = Solution()
abc.addTwoNumbers(l1.head,l2.head)
