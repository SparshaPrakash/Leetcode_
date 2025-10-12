class Solution {
    public int search(int[] nums, int target) {
        return bs(nums, target, 0, nums.length - 1);
    }
    private int bs(int[] a, int t, int lo, int hi) {
        if (lo > hi) return -1;
        int mid = lo + (hi - lo) / 2;
        if (a[mid] == t) return mid;
        if (a[mid] < t) return bs(a, t, mid + 1, hi);
        return bs(a, t, lo, mid - 1);
    }
}
