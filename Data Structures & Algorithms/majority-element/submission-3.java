class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> countMap = new HashMap();
        for (int v : nums) {
            if (countMap.containsKey(v)) {
                int value = countMap.get(v);
                countMap.put(v, value + 1);
            }
            else {
                countMap.put(v, 1);
            }
        }

        int max = 0;
        int resultKey = nums[0];
        int[] keys = countMap.keySet().stream().mapToInt(Integer::intValue).toArray();
        for (int k : keys) {
            int value = countMap.get(k);

            if (value > max) {
                resultKey = k;
                max = value;
            } 

        }
        return resultKey;
    }
}