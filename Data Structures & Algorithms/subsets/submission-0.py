class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        results = []

        subset = []

        def backtrack(index):

            if index == len(nums):
                results.append(subset[:])
                return
            
            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop()

            backtrack(index + 1)

        backtrack(0)
        return results