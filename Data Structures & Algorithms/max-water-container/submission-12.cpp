class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;
        int max_area = 0; // max value 

        while (l < r) {
            int distance = r - l;
            int current_area = distance * std::min(heights[l], heights[r]);
            max_area = std::max(max_area, current_area);
            
            if (heights[l] < heights[r]) {
                l += 1;
            }
            else {
                r -= 1;
            }
        }

        return max_area;
    }
};
