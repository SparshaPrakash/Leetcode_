class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # we get every i value in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # we now get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # Check if there are any rows or columns left to process.
            # If not, break the loop to avoid re-processing or accessing out-of-bounds elements.
            if not (left < right and top < bottom):
                break

            # here we get every i value in the bottom row
            for i in range(right -1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # get veery i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res