# class TrieNode(object):
#     def __init__(self):
#         self.children = {}
#         self.is_word = False

# class Trie(object):
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, word):
#         curr = self.root
#         for ch in word:
#             if ch not in curr.children:
#                 curr.children[ch] = TrieNode()
#             curr = curr.children[ch]
#         curr.is_word = True
    
#     def search(self, word):
#         def helper(word, idx, node):
#             # import pdb; pdb.set_trace()
#             if idx == len(word):
#                 return node.is_word
#             curr_ch = word[idx]
#             if curr_ch == '.':
#                 for _, next_node in node.children.items():
#                     if helper(word, idx+1, next_node):
#                         return True
#                 return False
#             if curr_ch in node.children:
#                 return helper(word, idx+1, node.children[curr_ch])
#             return False
            
#         return helper(word, 0, self.root)

# class WordDictionary(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = Trie()

#     def addWord(self, word):
#         """
#         Adds a word into the data structure.
#         :type word: str
#         :rtype: None
#         """
#         self.trie.insert(word)
        
#     def search(self, word):
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         :type word: str
#         :rtype: bool
#         """
#         return self.trie.search(word)


class TrieNode():
    
    def __init__(self):
        self.child = {}
        self.is_word = False


class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    
    def add_word(self, word):
        node = self.root
        
        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.is_word = True
    
    def search(self, word):
        
        def helper(word, idx, node):
            if idx == len(word):
                return node.is_word
            # curr_ch = word[idx]
            
            for x in range(idx, len(word)):
                curr_ch = word[x]
                if curr_ch == ".":
                    for _, child_node in node.child.items():
                        if helper(word, x+1, child_node):
                            return True
                    return False

                elif curr_ch in node.child:
                    node = node.child[curr_ch]
                    # return helper(word, idx+1, node.child[curr_ch])
                else:
                    return False
            return node.is_word
        
        return helper(word, 0, self.root)
                    

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.trie.add_word(word)
        
        
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.trie.search(word)
        
    
obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dad')
obj.addWord('mad')
obj.addWord('pad')

# print obj.search('a')
# print obj.search('a.')
# print obj.search('ab')
# print obj.search('.a')
# print obj.search('.b')
# print obj.search('ab.')
# print obj.search('.')
print (obj.search('bad'))