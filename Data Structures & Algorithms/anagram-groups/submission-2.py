class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        master_dict = {}

        curr_idx = 0

        for word in strs:

            freq_list = [0]*26
            
            for char in word:

                curr_char = ord(char) - ord("a")
                
                print(curr_char)

                freq_list[curr_char] += 1

            freq_tuple = tuple(freq_list)
            
            print(freq_tuple)

            if freq_tuple in master_dict:
                master_dict[freq_tuple].append(curr_idx)
            else:
                master_dict[freq_tuple] = [curr_idx]

            curr_idx += 1

        final_list = []
        
        for indices in master_dict.values():

            curr_list = []

            for index in indices:
                curr_list.append(strs[index])
            
            final_list.append(curr_list)

        return final_list
            
