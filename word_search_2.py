class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_word = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
    
        row = len(board)
        col = len(board[0])
        
        trie = Trie()

        for word in words:
            trie.add_word(word)
        
        node = trie.root
        ans = []

        def dfs(i, j, node, board, formed):
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] == "#":
                return
            
            char = board[i][j]
            
            if char not in node.children:
                return
            
            node = node.children[char]
            formed += char

            if node.is_word:
                ans.append(formed)
                node.is_word = False
            
            board[i][j] = "#"

            for x, y in [(0,1), (1,0), (-1, 0), (0,-1)]:
                dfs(i+x, j+y, node, board, formed)
            
            board[i][j] = char

        for i in range(row):
            for j in range(col):
                dfs(i, j, node, board, "")
        
        return ans

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
abc = Solution()
print (abc.findWords(board, words))
