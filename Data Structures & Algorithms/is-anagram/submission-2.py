class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        s_counts = [0]*26
        t_counts = [0]*26

        for i in range(len(s)):

            curr_s = ord(s[i]) - ord("a")
            curr_t = ord(t[i]) - ord("a")

            s_counts[curr_s] += 1
            t_counts[curr_t] += 1
        
        return s_counts == t_counts

            