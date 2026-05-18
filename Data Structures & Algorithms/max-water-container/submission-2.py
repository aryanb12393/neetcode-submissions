class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1

        max_area = (right - left) * min(heights[left], heights[right])

        while left < right:
            
            multiplying_height = min(heights[left], heights[right])
            curr_area = (right - left) * multiplying_height

            if multiplying_height == heights[left]:
                left += 1
            
            else:
                right -= 1
            
            max_area = max(max_area, curr_area)
        
        return max_area
