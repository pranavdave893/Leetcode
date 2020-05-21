'''
- spend more time designing
- a trie is slower than brute force

1. design a solution in brute force
2. identify the runtime and space time
3. analyze the runtime and identify bottlenecks
  1. unnecessary work
  2. duplicate work
  3. unoptimizable work
4. then we look for algos/ds to alleviate the bottleneck
'''

"""
barbi
bazbx

query = ba*bx

repeated comaprision = bar*b
"""
class Dictionary:
    def __init__(self, words):
        self.trie = defaultdict(dict)
        for word in words:
            self.add(word)
        
    def is_match(self, query):
        def word_match(node, idx=0):
            if idx == len(query):
                return "." in node
            
            letter = query[idx]
            if letter == "*":
                return True in [ word_match(child, idx+1) for child in node.values() ]

            if letter not in node:
                return False

            return word_match(node[letter], idx+1)
            
        return word_match(self.trie)

    def add(self, word):
        curr = self.trie
        for idx, letter in enumerate(word):
            if letter not in curr:
                curr[letter] = {}

            curr = curr[letter]

        curr["."] = {}