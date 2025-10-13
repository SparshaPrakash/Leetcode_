class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length, cols = matrix[0].length;

        // 1) Binary search over rows to find the candidate row
        int top = 0, bot = rows - 1;
        while (top < bot) {
            int mRow = top + (bot - top) / 2;
            if (target > matrix[mRow][cols - 1]) {          // bigger than last in this row
                top = mRow + 1;
            } else if (target < matrix[mRow][0]) {          // smaller than first in this row
                bot = mRow - 1;
            } else {
                // target must be within this row's range
                top = bot = mRow;
            }
        }

        if (top > bot) return false;                        // no valid row
        int mRow = top;

        // 2) Binary search within the found row
        int l = 0, r = cols - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (target > matrix[mRow][m]) {
                l = m + 1;
            } else if (target < matrix[mRow][m]) {
                r = m - 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
