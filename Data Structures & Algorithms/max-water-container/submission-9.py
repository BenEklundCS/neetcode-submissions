class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # define two pointers at either side of the array
        l = 0
        r = len(heights) - 1
        max_area = 0 # var to store max seen so far

        # algorithm for finding the max area
        # move the pointers closer together calculating the area at each step
        # once they meet the algo should terminate as the max will be found

        while l < r:
            # area is the lower of the heights * the distance between the two heights

            area = (r - l) * min(heights[l], heights[r])
            max_area = max(area, max_area) # set max_area to area if it's > max_area

            # move the lower height pointer inward, as its height has 
            # already contributed to the max possible solution at that point

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

        