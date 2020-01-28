class TrieNode(object):
    def __init__(self):
        self.is_word = False 
        self.children = {}
        self.count = 0
    
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, count):
        node = self.root
        
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_word = True
        node.count -= count

    
    def get_sentences_from_node(self, node, ans, lst):
        if node.is_word:
            lst.append((node.count, ans))
                
        for next_node in node.children:
            self.get_sentences_from_node(node.children[next_node], ans+next_node, lst)

    def search(self, letters):
        node = self.root
        formed = ""
        lst = []
        for letter in letters:
            if letter not in node.children:
                return lst
            
            node = node.children[letter]
            formed += letter

        self.get_sentences_from_node(node, formed, lst)

        return [x[1] for x in sorted(lst)][:3]
    
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Trie()
        self.historical_sentence = ""
        self.dct = {}
        
        for sentence, count in zip(sentences, times):
            self.trie.insert(sentence, count)
            self.dct[sentence] = count
    
    def input(self, c):
        """
        :type c: str    
        :rtype: List[str]
        """
        if c == "#":
            self.trie.insert(self.historical_sentence, 1)
            self.historical_sentence = ""
            return []

        else:
            self.historical_sentence += c
            return self.trie.search(self.historical_sentence)


obj = AutocompleteSystem(["abc","abbc","a"],[3,3,3])
print (obj.input("b"))
print (obj.input("c"))
print (obj.input("#"))
print (obj.input("b"))
print (obj.input("c"))
print (obj.input("#"))
print (obj.input("a"))
print (obj.input("b"))
print (obj.input("c"))
print (obj.input("#"))
print (obj.input("a"))
print (obj.input("b"))
print (obj.input("c"))
print (obj.input("#"))