class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_water = 0

        while start < end:
            smaller = min(heights[start], heights[end])
            distance = end - start
            max_water = max(smaller * distance, max_water)
            if smaller == heights[start]:
                start += 1
            else:
                end -= 1
        return max_water

        