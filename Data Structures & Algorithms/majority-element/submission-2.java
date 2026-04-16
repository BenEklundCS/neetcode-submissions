class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        int majorityElement = 0; // dummy val
        for (int i = 0; i < nums.length; i++) {
            if (count == 0) {
                majorityElement = nums[i];
            }
            count += nums[i] == majorityElement ? 1 : -1;
        }
        return majorityElement;
    }
}