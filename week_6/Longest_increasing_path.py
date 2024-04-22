class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])  
        memory = {} 

        def dfs(r, c, prevVal):
        
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
                return 0
 
            if (r, c) in memory:
                return memory[(r, c)]

            ans = 1  

            ans = max(ans, 1 + dfs(r + 1, c, matrix[r][c]))  
            ans = max(ans, 1 + dfs(r - 1, c, matrix[r][c])) 
            ans = max(ans, 1 + dfs(r, c + 1, matrix[r][c]))  
            ans = max(ans, 1 + dfs(r, c - 1, matrix[r][c]))  
            memory[(r, c)] = ans  
            return ans 
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)  
        return max(memory.values())  