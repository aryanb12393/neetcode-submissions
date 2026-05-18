import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max_val = max(piles)
        res = max_val

        while l <= r:

            mid = (l+r) // 2
            
            curr = 0

            for pile in piles:
                time = math.ceil(pile/mid)
                curr += time

            if curr <= h:
                res = min(res, mid)
                r = mid -1
            
            else:
                l = mid + 1


        return res