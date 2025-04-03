class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # saving the topleft
                topLeft = matrix[top][l + i]  

                # moving bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # moving bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # moving top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # moving top left into top right
                matrix[top + i][r] = topLeft

            r -= 1
            l += 1
