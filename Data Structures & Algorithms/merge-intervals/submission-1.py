class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i: i[0])

        res = [intervals[0]]
        # print(intervals)

        for start, end in intervals[1:]:
            
            prev = res[-1]
            last_start = prev[0]
            last_end = prev[1]

            print(last_end)

            if last_end >= start:
                res[-1] = [last_start, max(last_end, end)]
            else:
                res.append([start, end])
        
        return res