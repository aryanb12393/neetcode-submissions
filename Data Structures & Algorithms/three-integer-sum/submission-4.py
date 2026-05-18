class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = set()

        for i in range(len(nums)):

            target = -nums[i]
            j, k = i + 1, len(nums) - 1

            while j < k:
                curr_val = nums[j] + nums[k]

                if curr_val == target:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif curr_val < target:
                    j += 1
                else:
                    k -= 1

        return [list(t) for t in res]