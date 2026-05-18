class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        the_dict = {}

        for num in nums:

            if (num not in the_dict):
                the_dict[num] = 1
            else:
                return True
        
        return False