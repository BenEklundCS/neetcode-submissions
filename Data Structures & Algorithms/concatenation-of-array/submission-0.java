class Solution {
    public int[] getConcatenation(int[] nums) {
        int length = nums.length;
        int[] newArray = new int[length * 2]; // all 0's?
        for (int i = 0; i < nums.length; i++) {
            newArray[i] = nums[i];
            newArray[i + length] = nums[i];
        }
        return newArray;
    }
}