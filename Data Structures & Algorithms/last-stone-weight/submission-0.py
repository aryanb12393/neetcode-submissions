class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stones.sort()
            top_stone = heapq.heappop(stones)
            second_stone = heapq.heappop(stones)


            if second_stone > top_stone:
                heapq.heappush(stones, top_stone - second_stone)
        
        return -stones[0] if stones else 0