class Solution {
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;

        while (left < right) {
            // move left to next letter/digit
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            // move right to previous letter/digit
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            char cL = Character.toLowerCase(s.charAt(left));
            char cR = Character.toLowerCase(s.charAt(right));
            if (cL != cR) return false;

            left++;
            right--;
        }
        return true;
    }
}
