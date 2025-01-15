from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        result = []
        diagonals = {}

        # Group elements by their diagonals (i + j)
        for i in range(rows):
            for j in range(cols):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(mat[i][j])

        # Process diagonals and add to result
        for k in range(len(diagonals)):
            if k % 2 == 0:
                result.extend(reversed(diagonals[k]))  # Reverse for even diagonals
            else:
                result.extend(diagonals[k])           # Keep order for odd diagonals

        return result
