class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] magazineCount = new int[26];

        for (char c : magazine.toCharArray()) {
            magazineCount[(int)c - 'a'] += 1;
        }

        for (char c : ransomNote.toCharArray()) {
            if (magazineCount[(int)c - 'a'] == 0) return false;
            magazineCount[(int)c - 'a'] -= 1;
        }

        return true;
    }
}