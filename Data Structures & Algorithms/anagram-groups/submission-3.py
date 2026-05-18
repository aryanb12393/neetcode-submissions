class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        table = {}

        for i, word in enumerate(strs):
            
            bucket = [0] * 26

            for c in word:

                curr_idx = ord(c) - ord("a")
                bucket[curr_idx] += 1
            
            bucket_tuple = tuple(bucket)

            if bucket_tuple not in table:
                table[bucket_tuple] = []
            
            table[bucket_tuple].append(i)
        
        res = list(table.values())

        print(res)

        for i in range(len(res)):
            
            curr_row = res[i]

            for j in range(len(curr_row)):
                
                # print(i, j)
                # print(res[i][j])
                res[i][j] = strs[res[i][j]]
        
        return res








        