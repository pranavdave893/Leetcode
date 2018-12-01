from linked_list import Node

node = Node()
node.insert_at_beginning(5)
node.insert_at_beginning(4)
node.insert_at_beginning(2)
node.insert_at_beginning(1)

def insert_in_sorted_list(node,item):
    previous = None
    current = node.head
    stop = False

    while current != None and not stop:
        if current.data > item:
            stop = True
        else:
            previous = current
            current = current.next
    
    temp = Node(item)
    if previous == None:
        temp.next = node.head
        node.head = temp
    else:
        temp.next = current
        previous.next = temp

insert_in_sorted_list(node,3)
insert_in_sorted_list(node,0)
insert_in_sorted_list(node,6)
node.print_list()



