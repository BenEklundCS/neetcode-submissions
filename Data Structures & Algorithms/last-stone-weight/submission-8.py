class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        # make a max heap
        for i in range(len(stones)):
            stones[i] = -stones[i]
        stoneHeap = stones
        heapq.heapify(stoneHeap)
        while len(stones) > 1:
            # pop 2 and smash them
            x = heapq.heappop(stoneHeap)
            y = heapq.heappop(stoneHeap)
            if x != y:
                heapq.heappush(stoneHeap, -(y-x))
        return -stoneHeap[0] if len(stoneHeap) == 1 else 0