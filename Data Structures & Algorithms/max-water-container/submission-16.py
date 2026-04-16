class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_area = 0

        while l < r:
            # do some calculation on the two pointers
            min_height = min(heights[l], heights[r])
            distance = r - l
            area = min_height * distance

            # store the result of the calculation in max if its the max
            max_area = max(max_area, area)

            # decide how we want to move the pointers
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
                