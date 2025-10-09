class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int beg = 0, end = numbers.length - 1;
        while (beg < end) {
            int total = numbers[beg] + numbers[end];
            if (total == target) return new int[] { beg + 1, end + 1 }; // 1-based indices
            if (total > target) end--;
            else beg++;
        }
        return new int[] { -1, -1 }; // if no pair found
    }
}
