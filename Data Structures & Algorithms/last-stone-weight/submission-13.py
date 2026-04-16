class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We have to choose the two heaviest stones, we'll want a Max Heap
        # To create a max heap, multiply the list by -1 and then heapify
        for i in range(len(stones)):
            stones[i] *= -1
        
        stoneHeap = stones
        heapq.heapify(stoneHeap)
        while len(stones) > 1:
            # pop 2 and smash them
            x = heapq.heappop(stoneHeap)
            y = heapq.heappop(stoneHeap)
            if x != y:
                heapq.heappush(stoneHeap, -(y-x))
        return -stoneHeap[0] if len(stoneHeap) == 1 else 0