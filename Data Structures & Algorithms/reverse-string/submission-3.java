class Solution {
    public void reverseString(char[] s) {
        // define two points "setup step"
        int l = 0;
        int r = s.length - 1;

        // exit condition, when have we solved the problem?
        while (l < r) {
            // action: at each "step" what must be done
            char temp = s[r];
            s[r] = s[l];
            s[l] = temp;
            // move the pointers after each "action"
            l += 1;
            r -= 1;
        }
    }
}