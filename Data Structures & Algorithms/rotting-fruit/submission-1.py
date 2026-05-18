class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        has_fresh = False
        queue = deque()

        ripe = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    ripe += 1
                    has_fresh = True
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        # there are only rotten oranges / empty cells
        if not has_fresh:
            return 0
        
        # there are no rotten oranges
        if not queue:
            return -1
        
        minutes = 0

        def is_valid_cell(row, col):
            if 0 <= row < rows and 0 <= col < cols:
                return True
            return False

        def find_neighbours(row, col):
            
            # print("row and col")
            # print(row, col)

            directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

            res = []

            for direction in directions:

                x_coord = direction[0]
                y_coord = direction[1]

                nx, ny = row + x_coord, col + y_coord

                if is_valid_cell(nx, ny):
                    # print("yo")
                    res.append((nx, ny))

            return res

        # print(queue)
        infected = 0
        minutes = 0

        while queue:

            size = len(queue)
            
            # print(node)

            
            infected_this_round = False

            for _ in range(size):

                node = queue.popleft()
                node_neighbours = find_neighbours(node[0], node[1])

                for neighbour in node_neighbours:

                    curr_x = neighbour[0]
                    curr_y = neighbour[1]

                    cell = grid[curr_x][curr_y]

                    if cell == 1:
                        grid[curr_x][curr_y] = 2
                        queue.append(neighbour)
                        infected_this_round = True
                   
            if infected_this_round == True:
                minutes += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return minutes