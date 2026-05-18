class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        the_dict = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            curr_num = nums[i]

            if curr_num in the_dict:
                #if i != the_dict[curr_num]:
                return [the_dict[curr_num], i]
            
            the_dict[complement] = i

        
        print(the_dict)