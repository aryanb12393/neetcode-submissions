class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def check_invalid(i, j):

            if i < 0 or i >= len(grid):
                return True
            
            if j < 0 or j >= len(grid[0]):
                return True

            if grid[i][j] != 1:
                return True
            
            return False

        # islands = []
        vals = []

        def dfs(i, j):

            if check_invalid(i, j):
                return 0
            
            grid[i][j] = 0
            # hi += 1
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        
        best = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # print("yo")
                    # islands.append((i,j))
                    # hi = 0
                    best = max(best, dfs(i, j))

        return best
        
        # print(islands)
        # print(max(vals))
        #return max(vals)
