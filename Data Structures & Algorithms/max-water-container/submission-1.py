class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1

        max_area = (right-left) * min(heights[left], heights[right])

        while left <= right:
            
            min_height = min(heights[left], heights[right])

            curr_area = (right-left) * min_height

            if curr_area > max_area:
                max_area = curr_area

            if min_height == heights[left]:
                left += 1
            
            else:
                right -= 1
        
        return max_area
