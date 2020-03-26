from collections import defaultdict

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.nxt = None

class DLinkList(object):
    def __init__(self):
        self.dummy = Node(None, None)
        self.dummy.nxt = self.dummy.prev = self.dummy
        self.size = 0
    
    def append_left(self, node):
        node.nxt = self.dummy.nxt
        node.prev = self.dummy
        node.nxt.prev = node
        self.dummy.nxt = node
        self.size += 1
    
    def pop(self, node=None):
        if self.size == 0:
            return

        if not node:
            node = self.dummy.prev
        
        node.prev.nxt = node.nxt 
        node.nxt .prev = node.prev
        node.nxt  = node.prev = None
        self.size -= 1

        return node
    

class LFUCache(object):

    def __init__(self, capacity):
        self.size = 0
        self.cap = capacity
        self.freq = defaultdict(DLinkList)
        self.dct = {}
        self.min_freq = 0
    
    def update_dct(self, node):
        freq = node.freq
        
        self.freq[freq].pop(node)

        if self.min_freq == freq and freq not in self.freq:
            self.min_freq += 1
        
        node.freq += 1
        self.freq[node.freq].append_left(node)

    def get(self, key):
        if key not in self.dct:
            return -1
        
        node = self.dct[key]
        self.update_dct(node)
        return node.val
    
    def put(self, key, value):
        if self.cap == 0:
            return 

        if key in self.dct:
            node = self.dct[key]
            self.update_dct(node)
            node.val = value
        
        else:
            if self.size == self.cap:
                node = self.freq[self.min_freq].pop()
                del self.dct[node.key]
                self.size -= 1

            node = Node(key, value)
            self.dct[key] = node
            self.freq[1].append_left(node)
            self.min_freq = 1
            self.size += 1
    

abc = LFUCache(2)
abc.put(1, 1)
abc.put(2, 2)
abc.get(1)
abc.put(3, 3)
abc.get(2)
abc.get(3)
abc.put(4, 4)
abc.get(1)
abc.get(3)
abc.get(4)
