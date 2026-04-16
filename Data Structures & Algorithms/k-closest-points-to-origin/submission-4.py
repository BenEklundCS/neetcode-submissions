class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Solve the problem using a min heap
        minHeap = []
        # Destructure each point (x,y)
        for x, y in points:
            dist = (x ** 2) + (y ** 2) # Calculate the distance from the origin
            # Add to the heap
            minHeap.append([dist, x, y])
        # Heapify!
        heapq.heapify(minHeap)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res


