# from collections import deque
# class Node:
#     def __init__(self, k, v):
#         self.key = k
#         self.value = v
#         self.next = None
#         self.prev = None
        
# class LRUCache(object):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.cap = capacity
#         self.cache = dict()
#         self.head = Node(0,0)
#         self.tail = Node(0,0)
#         self.head.next = self.tail
#         self.tail.prev = self.head        

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         # import pdb; pdb.set_trace()
#         if key in self.cache:
#             node = self.cache[key]
#             self._remove(node)
#             self._add(node)
#             return node.value
#         return -1
        

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         # import pdb; pdb.set_trace()
#         if key in self.cache:
#             self._remove(self.cache[key])
        
#         elif len(self.cache) == self.cap:
#             node = self.head.next # remove Least recently used node.
#             self._remove(node)
#             del self.cache[node.key]
        
#         node = Node(key, value)
#         self._add(node)
#         self.cache[key] = node
    
#     def _add(self, node):
#         # import pdb; pdb.set_trace()
#         mru = self.tail.prev
#         mru.next = node
#         self.tail.prev = node
#         node.prev = mru
#         node.next = self.tail
    
#     def _remove(self, node):
#         # import pdb; pdb.set_trace()
#         prev_n = node.prev
#         prev_n.next = node.next
#         node.next.prev = prev_n


class LinkedList:
    
    def __init__(self, key, value, nxt=None, prev=None):
        self.key = key
        self.value = value
        self.nxt = nxt
        self.prev = prev
    
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dct = {}
        self.head = LinkedList(0, 0)
        self.tail = LinkedList(0, 0)
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.curr_cache_size = len(self.dct)
        

    def get(self, key: int) -> int:
        if key in self.dct:
            return self.remove_and_insert_node(key)
        
        return -1
            

    def put(self, key: int, value: int) -> None:
        
        if key in self.dct:
            self.remove_and_insert_node(key, value)
        
        elif self.curr_cache_size < self.capacity:
            self.insert_node(key, value)
        
        else:
            lru = self.head.nxt
            self.delete_node(lru.key, lru)
            self.insert_node(key, value)
        
        
    
    def delete_node(self, key, node):
        prev = node.prev
        node_next = node.nxt
        prev.nxt = node_next
        node_next.prev = prev
        node.nxt, node.prev = None, None
        self.curr_cache_size -= 1
        del self.dct[key]
    
    
    def insert_node(self, key, value):
        node = LinkedList(key, value)
        self.dct[key] = node
        mru = self.tail.prev
        mru.nxt = node
        node.nxt = self.tail
        node.prev = mru
        self.tail.prev = node
        self.curr_cache_size += 1
        return node
    
    
    def get_node(self, value):
        return self.dct[value]
    
    
    def remove_and_insert_node(self, key, value=None):
        node = self.get_node(key)
        value = node.value if not value else value
        
        self.delete_node(key, node)
        new_node = self.insert_node(key, value)

        return new_node.value


cache = LRUCache(1)
print (cache.put(2, 1))
# print (cache.put(2, 2))
print (cache.get(2))        # returns 1
print (cache.put(3, 2))    # evicts key 2
print (cache.get(2))       # returns -1 (not found)
# print (cache.put(4, 4))    # evicts key 1
# print (cache.get(1))       # returns -1 (not found)
print (cache.get(3))       # returns 3
# print (cache.get(4))       # returns 4