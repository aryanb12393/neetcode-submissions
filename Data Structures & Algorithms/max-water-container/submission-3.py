class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1

        curr_max = min(heights[left], heights[right]) * (right - left)

        while left < right:

            curr_height = min(heights[left], heights[right]) * (right - left)

            curr_max = max(curr_max, curr_height)

            if heights[left] < heights[right]:
                left += 1
            
            else:
                right -= 1
        
        return curr_max
