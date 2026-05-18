class Solution:    
    def search(self, nums: List[int], target: int) -> int:

        def find_pivot(nums):

            left = 0
            right = len(nums) - 1

            while left < right:

                mid = (left + right) // 2
                
                if nums[mid] > nums[right]:
                    left = mid + 1
                
                else:
                    right = mid

            return left

        pivot = find_pivot(nums)
        
        n = len(nums)

        left = 0
        right = len(nums) - 1

        while left <= right:
            
            mid = (left + right) // 2
            real_mid = (mid + pivot) % n

            if nums[real_mid] == target:
                return real_mid
            
            if nums[real_mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1

        return -1
        
        