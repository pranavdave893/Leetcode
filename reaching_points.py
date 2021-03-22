from collections import deque

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        q = deque()
        q.append((sx, sy))
        
        while q:
            x, y = q.popleft()
            
            if (x, y) == (tx, ty):
                return True
            
            print (x, y)
            if x > tx or y > ty:
                continue
            
            q.append((x, x+y))
            q.append((x+y, y))
        
        return False

abc = Solution()
abc.reachingPoints(1, 1, 3, 5)