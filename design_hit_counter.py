from collections import deque

class HitCounter(object):

    def __init__(self):
        self.dq = deque()
        self.curr_count = 0
    
    def hit(self, timestamp):
        if not self.dq or self.dq[-1][0] != timestamp:
            self.dq.append([timestamp, 1])
        else:
            self.dq[-1][1] += 1
        
        self.curr_count += 1
    
    def getHits(self, timestamp):
        while self.dq and self.dq[0][0] <= timestamp-300:
            self.curr_count -= self.dq.popleft()[1]
        
        return self.curr_count
            