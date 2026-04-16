class Solution {
    // global data
    List<List<Integer>> res;


    private List<List<Integer>> backtrack(List<Integer> perm, int[] nums, boolean[] pick) {
        // if reject(P, c) then return
        if (perm.size() == nums.length) {
            res.add(new ArrayList<>(perm));
            return res;
        }
        for (int i = 0; i < nums.length; i++) {
            if (!pick[i]) {
                perm.add(nums[i]);
                pick[i] = true;
                backtrack(perm, nums, pick);
                perm.remove(perm.size() - 1);
                pick[i] = false;
            }
        }
        return res;
    }

    public List<List<Integer>> permute(int[] nums) {
        res = new ArrayList<>();
        backtrack(new ArrayList<>(), nums, new boolean[nums.length]);
        return res;
    }
}
