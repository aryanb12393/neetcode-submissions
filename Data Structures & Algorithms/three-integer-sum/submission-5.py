class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        print(nums)
        res = set()

        for i, value in enumerate(nums):

            j = i + 1
            k = len(nums) - 1

            comp = value - 2 * value

            print(i, j, k)
            print(comp)

            while j < k:

                curr_sum = nums[j] + nums[k]

                if curr_sum == comp:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                
                elif curr_sum < comp:
                    j += 1
                
                else:
                    k -= 1
                # print("nums j is ", nums[j])
                # print("nums k is ", nums[k])
                # print("the current sum is ", curr_sum)
                # j += 1


            #     if curr_sum == comp:
            #         res.append([i, j, k])
                
            #     elif curr_sum > comp:
            #         k -= 1
                
            #     else:
            #         j += 1
        
        return list(res)


        