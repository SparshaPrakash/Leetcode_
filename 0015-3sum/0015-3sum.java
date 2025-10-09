import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length < 3) return res;

        Arrays.sort(nums); // sort first

        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // skip duplicate anchors

            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int total = nums[i] + nums[l] + nums[r];
                if (total > 0) {
                    r--;
                } else if (total < 0) {
                    l++;
                } else {
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++;
                    // skip duplicates on the left (mirrors your Python)
                    while (l < r && nums[l] == nums[l - 1]) l++;
                    // (optional) you can also do: r--; while (l < r && nums[r] == nums[r + 1]) r--;
                }
            }
        }
        return res;
    }
}
