class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int last = m + n - 1;
        int l = m - 1;
        int r = n - 1;

        while (l >= 0 && r >= 0) {
            if (nums1[l] > nums2[r]) {
                nums1[last] = nums1[l];
                l -= 1;
            } else {
                nums1[last] = nums2[r];
                r -= 1;
            }
            last -= 1;
        }

        while (r >= 0) {
            nums1[last] = nums2[r];
            r -= 1;
            last -= 1;
        }
    }
}