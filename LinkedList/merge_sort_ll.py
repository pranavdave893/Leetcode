"""
Merge sort of a linked list
"""

from linked_list import Node

node = Node()
node.insert_at_beginning(5)
node.insert_at_beginning(2)
node.insert_at_beginning(1)
node.insert_at_beginning(10)
node.insert_at_beginning(-1)
node.insert_at_beginning(30)
node.insert_at_beginning(12)
node.insert_at_beginning(6)

node.print_list()
    
def get_middle(head):
    slowptr = head
    fastptr = head

    while fastptr and fastptr.next:
        slowptr = slowptr.next
        fastptr = fastptr.next.next
    
    return slowptr

def sorted_merge(left, right):
    if not left:
        return right
    
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result  = right
        result.next = sorted_merge(left, right.next)
    
    return result

def merge_sort(head):
    import pdb; pdb.set_trace()
    if not head or not head.next:
        return head
    middle = get_middle(head)

    next_of_middle = middle.next
    middle.next = None

    left_part = merge_sort(head)
    right_part = merge_sort(next_of_middle)

    new_list = sorted_merge(left_part, right_part)

    return new_list

sorted_list = merge_sort(node)
sorted_list.print_list()


