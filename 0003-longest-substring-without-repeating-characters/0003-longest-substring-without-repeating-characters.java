import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen = new HashSet<>();
        int left = 0, maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            while (seen.contains(c)) {          // shrink until c is unique
                seen.remove(s.charAt(left));
                left++;
            }
            seen.add(c);                         // extend window
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
