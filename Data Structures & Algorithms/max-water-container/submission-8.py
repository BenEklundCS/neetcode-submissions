class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers, start and back of input array
        low = 0 
        high = len(heights) - 1
        # value to store max_area
        max_area = 0
        # loop while the pointers have not yet met
        while low < high:
            # find the area of the current container
            area = min(heights[low], heights[high]) * (high - low)
            # if the area is greater, set max_area to it
            max_area = max(area, max_area)
            # move the smallest pointer
                # why? Because we already know its value has contributed towards the only possible max from that point.
            if heights[low] <= heights[high]:
                low += 1
            else:
                high -= 1
        return max_area
