class Solution {
    public String mergeAlternately(String word1, String word2) {
        char[] mergeArray = new char[word1.length() + word2.length()];

        int idx = 0;
        int mergeIdx = 0;
        while (idx < word1.length() && idx < word2.length()) {
            mergeArray[mergeIdx] = word1.charAt(idx);
            mergeIdx += 1;
            mergeArray[mergeIdx] = word2.charAt(idx);
            mergeIdx += 1;
            idx += 1;
        }

        while (idx < word1.length()) {
            mergeArray[mergeIdx] = word1.charAt(idx);
            mergeIdx += 1;
            idx += 1;
        }

        while (idx < word2.length()) {
            mergeArray[mergeIdx] = word2.charAt(idx);
            mergeIdx += 1;
            idx += 1;
        }

        return String.valueOf(mergeArray);
    
    }
}