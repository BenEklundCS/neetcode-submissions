class Solution {
    public int removeDuplicates(int[] nums) {
        int l = 1; // "write" position
        for (int r = 1; r < nums.length; r++) {
            if (nums[r] != nums[r - 1]) {
                // then it's the "first time" we're seeing this value
                nums[l] = nums[r];
                l += 1;
            }
        }
        return l;
    }
}