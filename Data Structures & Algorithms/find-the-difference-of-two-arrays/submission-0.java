class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> inNums1 = new HashSet();
        Set<Integer> inNums2 = new HashSet();
        for (int n : nums1) {
            inNums1.add(n);
        }
        for (int n : nums2) {
            inNums2.add(n);
        }

        Set<Integer> notInNums1 = new HashSet();;
        Set<Integer> notInNums2 = new HashSet();
        for (int n : nums1) {
            if (!inNums2.contains(n)) {
                notInNums2.add(n);
            }
        }
        for (int n : nums2) {
            if (!inNums1.contains(n)) {
                notInNums1.add(n);
            }
        }
        return List.of(new ArrayList(notInNums2), new ArrayList(notInNums1));
    }
}