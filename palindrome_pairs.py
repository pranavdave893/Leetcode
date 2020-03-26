from collections import defaultdict
class Trie:
    def __init__(self):
        # letter -> next trie node.
        self.paths = defaultdict(Trie)
        self.wordEndIndex = -1
        self.palindromesBelow = []
    
    def isPalindrome(self, word):
        return word == word[::-1]
    
    def addWord(self, word, index):
        trie = self
        for j, char in enumerate(reversed(word)): 
            if self.isPalindrome(word[0:len(word)-j]):
                trie.palindromesBelow.append(index)
            trie = trie.paths[char]
        trie.wordEndIndex = index

class Solution(object):
    def isPalindrome(self, word):
        return word == word[::-1]

    def makeTrie(self, words):
        trie = Trie()
        for i, word in enumerate(words):
            trie.addWord(word, i)
        return trie

    def getPalindromesForWord(self, trie, word, index):
        output = []
        while word:
            if trie.wordEndIndex >= 0:
                if self.isPalindrome(word):
                    output.append(trie.wordEndIndex)
            if not word[0] in trie.paths:
                return output
            trie = trie.paths[word[0]]
            word = word[1:]

        if trie.wordEndIndex >= 0:
            output.append(trie.wordEndIndex)
        output.extend(trie.palindromesBelow)
        return output
                
    def palindromePairs(self, words):
        trie = self.makeTrie(words)
        output = []
        for i, word in enumerate(words):
            candidates = self.getPalindromesForWord(trie, word, i)
            output.extend([[i, c] for c in candidates if i != c])
        return output

abc = Solution()
abc.palindromePairs(["B", "BAN", "BANANA", "BAT", "MANA", "NAB", "NANA"])