class MyHashTable():
    
    def __init__(self, capacity):
        self.cap = capacity
        self.slot = [None] * capacity
    

    def hash_function(self, key):
        return key % self.cap
    

    def find_idx(self, key):
        idx = self.hash_function(key) 
        while self.slot[idx] is not None and self.slots[idx] != key:
            idx = (idx + 1) % self.cap
        return idx


    def insert(self, key):
        idx = self.find_idx(key)
        if self.slot[idx] != key:
            self.slot[idx] = key
            return 1
    

    def search(self, key):
        idx = self.find_idx(key)
        if self.slot[idx] != None:
            return self.slot[idx]
        return -1
        
        


    

        

    
