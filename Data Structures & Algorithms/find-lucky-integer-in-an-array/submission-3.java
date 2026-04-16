class Solution {
    public int findLucky(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int n : arr) {
            map.merge(n, 1, (oldV, newV) -> oldV + 1);
        }

        int largestLucky = -1;
        for (int n : arr) {
            int frequency = map.get(n);
            if (n == frequency) {
                largestLucky = Math.max(frequency, largestLucky);
            }
        }

        return largestLucky;
    }
}