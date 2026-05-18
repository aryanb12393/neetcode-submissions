class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        table = {}

        for i, val in enumerate(nums):
            table[val] = i
        
        for i in range(len(nums)):
            
            curr_num = nums[i]

            complement = target - curr_num

            if complement in table:
                
                if i != table[complement]:
                    return [i, table[complement]]

            
