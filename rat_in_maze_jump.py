
def RatInaMazeJump(M):
    if not M or not M[0]:
        return
    
    if M[-1][-1] != 1:
        return 0
    
    R = len(M)
    C = len(M[0])
    
    
    def is_valid(x, y, visited):
        return 0 <= x < R and 0 <= y < C and M[x][y] != 0 and (x, y) not in visited

    ans = 0 
    def dfs(r, c, ans, visited):
        if not is_valid(r, c, visited):
            return 0
        
        visited.add((r, c))

        if r == R-1 and c == C-1:
            ans+=1
            return ans
        
        for i in range(1, R):
            if i <= M[r][c]:
                
                ans = dfs(r+i, c, ans, visited)
                ans = dfs(r-i, c, ans, visited)
                ans = dfs(r, c+i, ans, visited)
                ans = dfs(r, c-i, ans, visited)
        return ans
                

    visited = set()    
    for r in range(R):
        for c in range(C):
            if is_valid(r, c, visited):
                ans = dfs(r, c, ans, visited)
                visited = set()
    
    return ans

M = [
    [2,1,0,0],
    [3,0,0,1],
    [0,1,0,1],
    [0,0,0,1]
]

print (RatInaMazeJump(M))