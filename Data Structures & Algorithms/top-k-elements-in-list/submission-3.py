class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        first_index_map = {}

        for i in range(len(nums)):
            
            curr_num = nums[i]

            if curr_num not in first_index_map:
                first_index_map[curr_num] = i

        freq_bucket = [0]*len(nums)

        for num in nums:
            
            num_idx = first_index_map[num]

            freq_bucket[num_idx] += 1
        
        # freq_map = {}

        correct_dict = {}

        for i, num in enumerate(freq_bucket):
            
            if num == 0:
                continue

            if num not in correct_dict:
                correct_dict[num] = [i]
            
            else:
                correct_dict[num].append(i)
        
        
        sorted_frequencies = sorted(correct_dict.keys(), reverse=True)

        final_list = []

        # print(correct_dict)
        # print("the most freq is ", most_freq)
        
        for freq in sorted_frequencies:

            if len(final_list) >= k:
                break

            curr_list = correct_dict[freq]

            for val in curr_list:
                if len(final_list) < k:
                    final_list.append(nums[val])
        
        return final_list
