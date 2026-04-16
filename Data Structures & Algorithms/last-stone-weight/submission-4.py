class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        stoneHeap = stones
        # This gives me a max heap of values
        heapq.heapify(stoneHeap)
        while len(stoneHeap) > 1:
            x = -heapq.heappop(stoneHeap)
            y = -heapq.heappop(stoneHeap)
            if x == y:
                continue # both are destroyed
            elif x < y:
                heapq.heappush(stoneHeap, -(y - x))
            else:
                heapq.heappush(stoneHeap, -(x - y))
        return -stoneHeap[0] if len(stoneHeap) == 1 else 0

