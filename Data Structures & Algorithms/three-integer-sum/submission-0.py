class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            complement = -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum < complement:
                    left += 1
                elif curr_sum > complement:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1

        return res