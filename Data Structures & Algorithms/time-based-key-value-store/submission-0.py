from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.my_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_map:
            self.my_map[key] = []

        self.my_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.my_map:
            return ""

        res = ""
        
        values = self.my_map[key]

        left = 0
        right = len(values) - 1

        while left <= right:
            
            mid = (left + right) // 2
            
            if values[mid][0] <= timestamp:
                 res = values[mid][1]
                 left = mid + 1
            else:
                right = mid - 1

        return res
        
