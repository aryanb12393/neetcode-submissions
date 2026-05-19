class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:

            mid = (top + bottom) // 2
            
            if matrix[mid][-1] < target:
                top = mid + 1
            
            elif target < matrix[mid][0]:
                bottom = mid - 1
            
            else:
                break

        if top > bottom:
            return False

        search_row = (top + bottom) // 2

        left = 0
        right = len(matrix[0]) - 1

        print(bottom)

        while left <= right:

            mid = (left + right) // 2
            
            curr_val = matrix[search_row][mid]

            if curr_val == target:
                return True
            
            elif curr_val < target:
                left = mid + 1
            
            else:
                right = mid - 1

        return False
 