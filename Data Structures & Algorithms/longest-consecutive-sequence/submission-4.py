class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        
        curr_max = 0

        for num in nums:
            
            # start counting from lowest number
            if num - 1 not in nums_set:

                seq = 1

                while num + seq in nums_set:

                    seq += 1
                
                curr_max = max(curr_max, seq)
                
        return curr_max




