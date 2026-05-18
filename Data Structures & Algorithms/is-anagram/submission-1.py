class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        s_counts = {}
        t_counts = {}

        for idx in range(len(s)):

            curr_char_s = s[idx]
            curr_char_t = t[idx]

            if curr_char_s not in s_counts:
                s_counts[curr_char_s] = 1
            else:
                s_counts[curr_char_s] += 1
            
            if curr_char_t not in t_counts:
                t_counts[curr_char_t] = 1
            else:
                t_counts[curr_char_t] += 1
        

        print(s_counts, t_counts)
        return (s_counts == t_counts)