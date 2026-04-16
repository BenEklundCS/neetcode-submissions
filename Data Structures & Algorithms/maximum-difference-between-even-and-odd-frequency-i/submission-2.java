class Solution {
    public int maxDifference(String s) {
        HashMap<Character, Integer> map = new HashMap();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            map.merge(c, 1, (oldV, newV) -> oldV + 1);
        }

        int maxOdd = 0;
        int minEven = Integer.MAX_VALUE;

        for (int value : map.values()) {
            System.out.println(value);
            if (value % 2 == 0 && value < minEven) {
                minEven = value;
            }
            else if (value % 2 != 0 && value > maxOdd) {
                maxOdd = value;
            }
        }

        return maxOdd - minEven;
    }
}