from doubly_linked_list import Node

class LRUcache(object):
    
    def __init__(self,size=None):
        self.cache_list = Node()
        self.cache_table = {}
        self.size = size
    
    def put(self,value):
        if value in self.cache_table:
            new_node = self.cache_table[value]
            if new_node == self.cache_list.tail:
                return
            elif new_node == self.cache_list.head:
                self.cache_list.delete_with_data(new_node)
                self.cache_list.insert_at_end(new_node)
            else:
                self.cache_list.tail.prev.next = new_node
                new_node.prev.next =  self.cache_list.tail #1
                new_node.next.prev =  self.cache_list.tail #2
                self.cache_list.tail.next = new_node.next #3
                self.cache_list.tail.prev.next = new_node #4
                new_node.prev, self.cache_list.tail.prev = self.cache_list.tail.prev, new_node.prev # 5 and 6
                new_node.next =  None # 7
                self.cache_list.tail = new_node #8
        else:
            new_node = Node(value,None,None)
                
            if self.cache_list.length < self.size:
                self.cache_list.insert_at_end(value)
                self.cache_table[value] = self.cache_list.tail
            else:
                del self.cache_table[self.cache_list.head.data]
                self.cache_list.delete_from_beginning()
                self.cache_list.insert_at_end(value)
                self.cache_table[value] = self.cache_list.tail
    
    def get(self,value):
        if value in self.cache_table:
            node = self.cache_table[value]
            print node.data
        else:
            return -1

x = LRUcache(size=4)
x.put(1)
x.put(2)
x.put(3)
x.put(4)
x.put(2)
x.get(2)
print True

