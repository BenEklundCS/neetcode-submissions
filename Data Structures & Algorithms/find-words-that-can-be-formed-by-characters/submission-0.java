class Solution {
    public int countCharacters(String[] words, String chars) {
        Map<Character, Integer> charFreq = new HashMap<>(); 

        for (int i = 0; i < chars.length(); i++) {
            charFreq.merge(chars.charAt(i), 1, (o, n) -> o + 1);
        }

        int count = 0;
        for (String s : words) {
            if (isGood(s, charFreq)) {
                count += s.length();
            }
        }
        return count;
    }

    private boolean isGood(String s, Map<Character, Integer> charFreq) {
        Map<Character, Integer> wordCharFreq = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            wordCharFreq.merge(s.charAt(i), 1, (o, n) -> o + 1);
        }

        for (char c : wordCharFreq.keySet()) {
            if (!charFreq.containsKey(c) || wordCharFreq.get(c) > charFreq.get(c)) {
                return false;
            }
        }
        return true;
    }
}