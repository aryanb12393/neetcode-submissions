class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
            
        curr_set = set()

        for num in nums:
            curr_set.add(num)

        curr_max = 1

        for num in nums:
            
            curr_count = 1

            temp_num = num - 1

            while temp_num in curr_set:
                curr_count += 1
                temp_num -=1
            
            curr_max = max(curr_max, curr_count)

        return curr_max
