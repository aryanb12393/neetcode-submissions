class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        edge_o = []

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1) or (j == 0 or j == n-1):
                    if board[i][j] == "O":
                        edge_o.append((i, j))

        def is_valid(i, j):

            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            
            if board[i][j] == "X" or board[i][j] == "T":
                return False
            
            return True

        def dfs(i, j):
            
            if not is_valid(i, j):
                return
            
            # print("hello")

            board[i][j] = "T"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        
        for o in edge_o:
            # print(o)
            dfs(o[0], o[1])
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"