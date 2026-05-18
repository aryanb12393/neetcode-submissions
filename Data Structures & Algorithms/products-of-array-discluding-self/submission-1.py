class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_arr = [1] * len(nums)
        product = 1

        for i in range(len(nums)):
            left_arr[i] = product
            product *= nums[i]
            print(product)

        # print(left_arr)

        right_arr = [1] * len(nums)
        product = 1

        for i in range(len(nums)-1, -1, -1):
            right_arr[i] = product
            # print(product)
            product *= nums[i]

        res = []

        for i in range(len(nums)):

            res.append(left_arr[i] * right_arr[i])

        return res
       