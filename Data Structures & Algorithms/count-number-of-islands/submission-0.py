class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = {}

        def dfs(r,c):

            if r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[0]) - 1 or grid[r][c] == "0" or m.get((r,c)):
                return

            m[(r,c)] = True

            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):

                if grid[r][c] == "1" and (r,c) not in m:
                    
                    islands += 1
                    dfs(r,c)
                
        
        return islands


        