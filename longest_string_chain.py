class Solution(object):
    def longestStrChain_dp(self, words):
        
        def helper(word, cache, word_set):
            if word in cache:
                return cache[word]
            
            count = 0
            for i in range(len(word)):
                pre = word[:i] + word[i+1:]

                if pre in word_set:
                    count = max(count, helper(pre, cache, word_set))
            
            cache[word] = 1 + count
            return 1 + count

        cache = {}
        count = 0
        word_set = set(words)

        for word in words:
            max_chain = max(count, helper(word, cache, word_set))
        
        print (max_chain)

    def longestStrChain(self, words):
        dp = {}
        for w in sorted(words, key=len):
            max_len = 0
            for i in range(len(w)):
                pre = w[:i] + w[i+1:]
                max_len = max(max_len, dp.get(pre, 0)+1)
            dp[w] = max_len
        
        print(max(dp.values()))

abc = Solution()
abc.longestStrChain(["a","b","xy","xyz","ab","abc","abx","aby","abyxc"])
        
