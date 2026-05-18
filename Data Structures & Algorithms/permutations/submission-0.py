class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        results = []

        def backtrack(permutation, nums, pick):
            
            # hit the 3 length
            if len(permutation) == len(nums):
                results.append(permutation[:])
                return

            for i in range(len(nums)):

                if not pick[i]:
                    pick[i] = True
                    permutation.append(nums[i])
                    backtrack(permutation, nums, pick)
                    permutation.pop()
                    pick[i] = False
            
        pick = [False] * len(nums)
        backtrack([], nums, pick)
        return results

            