import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone1 = [-i for i in stones]
        heapq.heapify(stone1)

        while len(stone1) > 1:
            x = -1 * heapq.heappop(stone1)
            y = -1 * heapq.heappop(stone1)

            if x!=y:
                heapq.heappush(stone1 ,y-x)
            
        
        return -1 * heapq.heappop(stone1) if len(stone1) == 1 else 0