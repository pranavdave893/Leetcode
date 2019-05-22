class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        
        for letter in word:
            if word in curr.children:
                curr = curr.children[letter]
            else:
                new_node = TrieNode()
                curr.children[letter] = new_node
                curr = new_node
        
        curr.is_word = True

    def search(self, word):
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        
        return curr.is_word
    
    def startsWith(self, prefix):
        curr = self.root
        
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True