class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return []
        
        if not matrix[0]:
            return []

        x, y, d = 0, 0, 0 

        dirs = [(0,1), (1,0), (0, -1), (-1, 0)]
        
        visited = set()
        
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        res = []

        for i in range(num_rows * num_cols):

            cell = matrix[x][y]
            res.append(cell)
            visited.add((x,y))

            nx, ny = x + dirs[d][0], y + dirs[d][1]

            if (nx,ny) in visited or not (0 <= nx < num_rows and 0 <= ny < num_cols):
                d = (d+1) % 4
                nx, ny = x + dirs[d][0], y + dirs[d][1]

            x, y = nx, ny
    
            
            
        
        return res

            









