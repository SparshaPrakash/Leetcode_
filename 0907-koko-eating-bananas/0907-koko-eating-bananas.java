class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1, r = 0;
        for (int p : piles) r = Math.max(r, p);  // max pile as upper bound
        int res = r;

        while (l <= r) {
            int k = l + (r - l) / 2;  // candidate speed
            long hours = 0;           // use long to avoid overflow
            for (int p : piles) {
                // ceil(p / k) without floating point: (p + k - 1) / k
                hours += (p + k - 1) / k;
            }

            if (hours <= h) {
                res = k;
                r = k - 1;           // try smaller speed
            } else {
                l = k + 1;           // need faster speed
            }
        }
        return res;
    }
}
