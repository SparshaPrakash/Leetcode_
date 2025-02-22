class Solution:
    def minFallingPathSum(self, matrix):
        """
        Bottom-up approach to find the minimum falling path sum.
        :param matrix: List[List[int]] - square matrix of integers
        :return: int - the minimum falling path sum
        """
        N = len(matrix)

        for r in range(N - 2, -1, -1):  # Start from second-last row
            for c in range(N):
                mid = matrix[r + 1][c]  # Below cell
                left = matrix[r + 1][c - 1] if c > 0 else float("inf")  # Below-left
                right = matrix[r + 1][c + 1] if c < N - 1 else float("inf")  # Below-right
                matrix[r][c] += min(mid, left, right)  # Update the current cell

        return min(matrix[0])  # The answer is the min value in the first row
