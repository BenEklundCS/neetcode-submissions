class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] sc = new int[26];
        for (int i = 0; i < s.length(); i++) {
            sc[(int)s.charAt(i) - (int)'a'] += 1;
        }
        for (int j = 0; j < t.length(); j++) {
            sc[(int)t.charAt(j) - (int)'a'] -= 1;
        }
        for (int c : sc) {
            if (c != 0) return false;
        }
        return true;
    }
}
