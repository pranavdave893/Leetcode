from heapq import heappush, heappop, heapreplace, heapify
class MedianFinder(object):

    def __init__(self):
        #keep smaller half (size >= 1)
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
            

    def findMedian(self):
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        return ((-self.maxHeap[0] + self.minHeap[0] + 0.00 )/2)

abc = MedianFinder()
abc.addNum(1)
abc.addNum(2)
abc.addNum(3)
abc.addNum(0)
abc.addNum(-5)
print (abc.findMedian())
