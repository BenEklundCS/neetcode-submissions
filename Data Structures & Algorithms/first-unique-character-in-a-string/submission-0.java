class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> freq = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            freq.merge(s.charAt(i), 1, (o, n) -> o + 1);
        }

        for (int i = 0; i < s.length(); i++) {
            if (freq.get(s.charAt(i)) == 1) {
                return i;
            }
        }

        return -1;
    }
}