class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        max_len = 0
        seen = set()
        
        # seen.add(s[0])

        l = 0
        r = 0

        while r < len(s):
            
            print(seen)

            if s[r] not in seen:
                seen.add(s[r])
                max_len = max(max_len, r-l+1)
                r += 1
            
            else:
                
                seen.remove(s[l])
                l += 1

        return max_len
    