class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        gas = nums[0]

        for i in range(1, len(nums)):

            curr_val = nums[i]
            gas -= 1

            if gas < 0:
                return False

            if curr_val > gas:
                gas = curr_val
            

        
        return True

