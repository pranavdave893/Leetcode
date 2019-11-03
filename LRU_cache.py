from collections import deque
class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # import pdb; pdb.set_trace()
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # import pdb; pdb.set_trace()
        if key in self.cache:
            self._remove(self.cache[key])
        
        elif len(self.cache) == self.cap:
            node = self.head.next # remove Least recently used node.
            self._remove(node)
            del self.cache[node.key]
        
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
    
    def _add(self, node):
        # import pdb; pdb.set_trace()
        mru = self.tail.prev
        mru.next = node
        self.tail.prev = node
        node.prev = mru
        node.next = self.tail
    
    def _remove(self, node):
        # import pdb; pdb.set_trace()
        prev_n = node.prev
        prev_n.next = node.next
        node.next.prev = prev_n

cache = LRUCache(2)
print (cache.put(1, 1))
print (cache.put(2, 2))
print (cache.get(1))        # returns 1
print (cache.put(3, 3))    # evicts key 2
print (cache.get(2))       # returns -1 (not found)
print (cache.put(4, 4))    # evicts key 1
print (cache.get(1))       # returns -1 (not found)
print (cache.get(3))       # returns 3
print (cache.get(4))       # returns 4