class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}

        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
            
        buckets = [[] for i in range(len(nums))]

        for val, freq in freq_dict.items():
            # print(val, freq)
            buckets[freq-1].append(val)
        
        final_res = []

        for i in range(len(buckets)-1, -1, -1):
            
            curr_vals = buckets[i]

            for curr_val in curr_vals:

                if len(final_res) == k:
                    break
                
                final_res.append(curr_val)

        return final_res


        