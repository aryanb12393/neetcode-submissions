class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dict = {}

        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]  # index = frequency
        
        for num, freq in freq_dict.items():
            buckets[freq].append(num)

        res = []

        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                if len(res) < k:
                    res.append(num)
                else:
                    break
        
        return res