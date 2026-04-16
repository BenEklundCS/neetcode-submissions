class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_water = 0

        while start < end:
            distance = end - start
            area = min(heights[start], heights[end]) * distance
            max_water = max(area, max_water)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return max_water

        