class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        length = len(nums) * 2
        ans = [None] * length
        
        i = 0
        
        for num in nums:
            ans[i] = num
            i += 1
        
        for num in nums:
            ans[i] = num
            i += 1

        return ans