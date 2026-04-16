class Solution {
    public String kthDistinct(String[] arr, int k) {
        Map<String, Integer> countMap = new HashMap();

        for (String s : arr) {
            countMap.merge(s, 1, (o, n) -> o + 1);
        }

        for (String s : arr) {
            // distinct
            if (countMap.get(s) == 1) {
                k--;
                if (k == 0) {
                    return s;
                }
            }
        }

        return "";
    }
}