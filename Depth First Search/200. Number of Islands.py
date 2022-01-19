class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0     
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count +=1
        return count
        
    def dfs(self,grid, i,j):
        if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j]!="1":
            return
        grid[i][j] = '5'
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)

# Iterate all cells, for each cell, do a DFS
# The exit situation of the DFS is when index is out of bound, or the current cell is not an island
# Otherwise, if the current cell is still "1", change it to "5" (used as a flag, meaning this cell has been visited) 