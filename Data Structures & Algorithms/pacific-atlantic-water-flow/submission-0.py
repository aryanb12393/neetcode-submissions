class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])
        
        pac_set = set()
        atl_set = set()

        def dfs(row, col, curr_set, curr_height):

            curr_tuple = (row, col)
            
            if curr_tuple in curr_set:
                # print("hello")
                return

            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            
            # print(row, col, curr_set, curr_height)

            if heights[row][col] < curr_height:
                return

            curr_set.add((row, col))

            dfs(row + 1, col, curr_set, heights[row][col])
            dfs(row - 1, col, curr_set, heights[row][col])
            dfs(row, col + 1, curr_set, heights[row][col])
            dfs(row, col - 1, curr_set, heights[row][col])

        for c in range(cols):
            # first row
            dfs(0, c, pac_set, heights[0][c])
            # last row
            dfs(rows-1, c, atl_set, heights[rows-1][c])
        
        for r in range(rows):
            # first col
            dfs(r, 0, pac_set, heights[r][0])
            # last col
            dfs(r, cols-1, atl_set, heights[r][cols-1])

        
        return [[r, c] for r, c in pac_set & atl_set]
        
        

