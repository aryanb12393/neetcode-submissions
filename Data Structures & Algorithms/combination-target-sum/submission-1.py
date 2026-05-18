class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        results = []
        nums.sort()

        def backtrack(i, current_list, total):

            if total == target:
                results.append(current_list[:])
                return
            
            # if total > target:
            #     return
            
            # if i >= len(nums):
            #     return
            
            for j in range(i, len(nums)):

                if total + nums[i] <= target:
                    current_list.append(nums[j])
                    backtrack(j, current_list, total + nums[j])
                    current_list.pop()
                else:
                    return

            
        backtrack(0, [], 0)
        return results
