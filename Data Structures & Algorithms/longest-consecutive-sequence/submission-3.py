class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
            
        curr_set = set(nums)

        curr_max = 1

        for num in nums:
            
            #curr_count = 1

            # temp_num = num - 1

            # while temp_num in curr_set:
            #     curr_count += 1
            #     temp_num -=1

            if num - 1 not in curr_set:

                seq = 0

                while num + seq in curr_set:
                    seq += 1
            
                curr_max = max(curr_max, seq)

        return curr_max
