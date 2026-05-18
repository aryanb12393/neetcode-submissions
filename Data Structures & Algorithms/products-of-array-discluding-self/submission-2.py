class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_arr = [1] * len(nums)
        product = 1

        for i in range(len(nums)):
            left_arr[i] = product
            product *= nums[i]

        right_arr = [1] * len(nums)
        product = 1

        for i in range(len(nums) - 1, -1, -1):
            right_arr[i] = product
            product *= nums[i]

        res = []

        for val_1, val_2 in zip(left_arr, right_arr):
            res.append(val_1 * val_2)

        return res