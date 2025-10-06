import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (hashMap.containsKey(complement)) {
                return new int[] { i, hashMap.get(complement) };
            }
            hashMap.put(nums[i], i);
        }

        return new int[] {};  // return empty array if not found
    }
}
