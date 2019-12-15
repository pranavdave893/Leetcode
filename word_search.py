class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False
        
        R = len(board)
        C = len(board[0])
        start = 0
        visited = set()
        
        def dfs(start, i, j, visited):
            for x, y in [(0,1), (1,0), (-1, 0), (0,-1)]:
                xi = x+i
                yj = y+j
                if 0 <= xi < R and 0 <= yj < C and (xi,yj) not in visited and board[xi][yj] == word[start]:
                    print (xi, yj)
                    # if (xi, yj) == (2, 0):
                    #     import pdb; pdb.set_trace()
                    if start == len(word)-1:
                        return True
                    
                    visited.add((xi, yj))
                    result = dfs(start+1, xi, yj, visited)
                    if result:
                        return result
                    else:
                        visited.remove((xi, yj))
            return

        for i in range(R):
            for j in range(C):
                visited = set()
                if board[i][j] == word[start]:
                    # print ("start",i,j)
                    visited.add((i,j))
                    if start == len(word) -1:
                        return True
                    result = dfs(start+1, i, j, visited)
                    if result:
                        return result
                # else:
                #     visited = set()
        return False

# True
board_1 = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word_1 = "ABCEFSADEESE"

# True
board_2 = [["C","A","A"],["A","A","A"],["B","C","D"]]
word_2 = "AAB"

# False
board_3 = [["a", "a"]]
word_3 = "aaa"

# True
board_4 = [["a"]]
word_4 = "a"


abc = Solution()
assert abc.exist(board_1, word_1) = True
assert True ==  abc.exist(board_2, word_2))
assert False ==  abc.exist(board_3, word_3))