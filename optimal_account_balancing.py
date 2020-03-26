import collections
import Queue
class Solution(object):
    def minTransfers(self, transactions):
        def bfs(net):
            while q.qsize():
                t, path, start = q.get()
                if not t:
                    break
                for i in xrange(start, len(net)):
                    q.put((t+net[i], path+[i], i+1))
                    
            self.res += len(path)-1
            path = set(path)
            return [net[i] for i in xrange(len(net)) if i not in path]
            
        d = collections.Counter()
        for t in transactions:
            d[t[0]] += t[2]
            d[t[1]] -= t[2]
        net = [d[item] for item in d if d[item] != 0]
        
        self.res = 0
        while len(net):
            q = Queue.Queue()
            q.put((net[0], [0], 1))
            net = bfs(net)
        return self.res

abc = Solution()
print (abc.minTransfers([[0,1,5],[2,3,1],[2,0,1],[4,0,2]])) # 4
print (abc.minTransfers([[0,1,2],[1,2,1],[1,3,1]])) # 2
print (abc.minTransfers([[0,1,10], [1,0,1], [1,2,5], [2,0,5]])) # 1
print (abc.minTransfers([[0,1,10], [2,0,5]])) # 2