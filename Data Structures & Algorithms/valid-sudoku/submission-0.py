class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        grids = [[0,1,2], [3,4,5], [6,7,8]]
        final_grids = []
        for grid in grids:
            for grid2 in grids:
                final_grids.append([grid, grid2])
        
        for elt in final_grids:
            first_grid = elt[0]
            second_grid = elt[1]
            square_set = set()

            for r in first_grid:
                for c in second_grid:
                    curr_elt = board[r][c]
                    if curr_elt in square_set:
                        return False
                    if curr_elt != ".":
                        square_set.add(curr_elt)

                    #print(r,c)
            #print("square done")


        for r in range(9):

            row_set = set()

            for c in range(9):
                
                curr_elt = board[r][c]
                
                if curr_elt in row_set:
                    return False

                if curr_elt != ".":
                    row_set.add(curr_elt)

        
        # checks columns
    
        for r in range(9):

            col_set = set()

            for c in range(9):
                
                curr_elt = board[c][r]

                if curr_elt in col_set:
                    return False

                if curr_elt != ".":
                    col_set.add(curr_elt)
        
    
        return True