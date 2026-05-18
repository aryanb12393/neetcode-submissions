class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        the_dict = {}

        for i in range(len(nums)):
            
            complement = target - nums[i]

            if complement in the_dict:
                return [the_dict[complement], i]
            
            the_dict[nums[i]] = i

        return []