class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = {}
        best = 0
        n = len(grid)
        m = len(grid[0])

        def dfs(i,j) -> int:
            
            if i < 0 or i > n - 1  or j < 0 or j > m - 1:
                return 0
            if (i,j) in visited:
                return 0
            visited[(i,j)] = 1
            if grid[i][j] == 0:
                return 0
            
            left = dfs(i-1,j)
            right = dfs(i+1, j)
            up = dfs(i,j+1)
            down = dfs(i, j-1)

            return 1 + left + right + up + down
        
        for i in range(n):
            for j in range(m):
                if (i,j) in visited:
                    continue
                if grid[i][j] == 0:
                    visited[(i,j)] = 1
                    continue
                new = dfs(i,j)
                best = max(best, new)

        return best

