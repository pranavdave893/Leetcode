"""
Reverse a Linked List with O(1) space, without using recursion.
"""
import copy
from linked_list import Node

node = Node()
node.insert_at_beginning(1)
node.insert_at_end(2)
node.insert_at_end(3)
node.insert_at_end(4)
node.insert_at_end(5)

prev_node = None
next_node = node.head.next
while(True):
    node.head.next = prev_node
    if next_node == None:
        break
    prev_node = node.head
    node.head = next_node
    next_node = next_node.next

node.print_list()