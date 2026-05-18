class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        results = []

        def backtrack(i, current_list, total):

            if total == target:
                results.append(current_list[:])
                return
            
            if total > target:
                return
            
            if i >= len(nums):
                return
            
            current_list.append(nums[i])
            backtrack(i, current_list, total + nums[i])
            current_list.pop()

            backtrack(i + 1, current_list, total)

        backtrack(0, [], 0)
        return results
