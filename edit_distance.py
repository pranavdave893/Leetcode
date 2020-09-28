from collections import deque

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        q = deque()
        q.append((word1, 0))
        
        ans = 0
        new_ans = float('inf')
        
        while q:
            curr_word, ans = q.popleft()
            
            if curr_word == word2:
                return ans
            
            w1, w2 = 0, 0
            
            while w1 < len(curr_word) and w2 < len(word2) and curr_word[w1] == word2[w2]:
                w1 += 1
                w2 += 1
            
            if w2 >= len(word2):
                new_ans = min(ans + len(curr_word) - w1, new_ans)
                continue
                
            
            if w1 >= len(curr_word):
                new_ans = min(len(word2) - w2 + 1, new_ans)
                continue
            
            replace = curr_word[:w1] + word2[w2] + curr_word[w1+1:]
            delete = curr_word[:w1] + curr_word[w1+1:]
            insert = None
            if w1 != 0:
                insert = curr_word[:w1] + word2[w2] + curr_word[w1:]

            for next_words in [replace, delete, insert]:
                if next_words:
                    q.append((next_words, ans+1))
        
        return new_ans

abc = Solution()
print (abc.minDistance("horse", "ros"))