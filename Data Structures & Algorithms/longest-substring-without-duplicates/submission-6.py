class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        charset = set()
        max_len = 0
        l = 0
        r = 0


        while r < len(s):
            if s[r] not in charset:
                charset.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1
            else:
                charset.remove(s[l])
                l += 1

        return max_len