class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # row check
        for row in board:
            curr_row = set()
            for value in row:
                if value not in curr_row:
                    if value == ".":
                        continue
                    curr_row.add(value)
                else:
                    return False

        # column check

        for i in range(9):
            curr_col = set()
            for j in range(9):
                value = board[j][i]
                # print(value)
                if value not in curr_col:
                    if value == ".":
                        continue
                    curr_col.add(value)
                else:
                    return False

        # 00, 01, 02
        # 10, 11, 12
        # 20, 21, 22

        grid_centers = [1,4,7]

        def check_grid(x, y):
            
            grid_set = set()

            for i in range(x-1, x+2):

                for j in range(y-1, y+2):

                    if board[i][j] not in grid_set:

                        if board[i][j] == ".":
                            continue
                        
                        grid_set.add(board[i][j])
                    
                    else:
                        return False

            return True

            print("that was around ", x, y)

        for i in grid_centers:

            for j in grid_centers:

                if not check_grid(i, j):
                    
                    return False

        return True
        