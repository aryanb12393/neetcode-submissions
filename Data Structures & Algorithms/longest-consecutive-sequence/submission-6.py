class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        
        best = 0

        for num in nums:
            
            if num - 1 not in nums_set:

                curr_max = 1

                while num + 1 in nums_set:

                    curr_max += 1
                    num = num + 1
                
                best = max(curr_max, best)
        
        return best
            


