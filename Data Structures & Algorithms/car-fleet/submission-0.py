class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars_list = sorted(zip(position, speed), reverse = True)
        fleets = 0
        curr_time = 0

        for dist, speed in cars_list:

            time = (target-dist) / speed

            if curr_time < time:
                fleets += 1
                curr_time = time
            
        return fleets