import java.util.HashSet;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        HashSet<Integer> set = new HashSet<>();
        for (int n : nums) set.add(n);

        int maxLen = 0;

        for (int n : set) {
            // start a sequence only if n-1 doesn't exist (n is a sequence head)
            if (!set.contains(n - 1)) {
                int curr = n;
                int len = 1;

                while (set.contains(curr + 1)) {
                    curr++;
                    len++;
                }
                if (len > maxLen) maxLen = len;
            }
        }

        return maxLen;
    }
}
