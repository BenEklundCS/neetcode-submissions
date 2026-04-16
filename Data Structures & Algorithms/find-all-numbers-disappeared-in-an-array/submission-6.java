class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        // existance not count
        Set<Integer> set = new HashSet();

        for (int i = 1; i <= nums.length; i++) {
            set.add(i);
        }

        for (int i = 0; i < nums.length; i++) {
            set.remove(nums[i]);
        }

        return new ArrayList(set);
    }
}