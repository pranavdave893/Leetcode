from collections import Counter
import heapq

class FreqWord(object):
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __cmp__(self, other):
        if self.freq != other.freq:
            return cmp(self.freq, other.freq)
        else:
            return cmp(other.word, self.word)


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, FreqWord(freq, word))
            if len(heap) > k:
                heapq.heappop(heap)
        
        print ([heapq.heappop(heap).word for _ in xrange(k)][::-1])

words = ["i", "love", "leetcode", "i", "love", "coding"]
abc = Solution()
abc.topKFrequent(words, 2)



