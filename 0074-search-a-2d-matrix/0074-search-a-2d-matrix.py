class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        while top < bot:
            m_row = (top + bot) // 2
            if target > matrix[m_row][-1]:
                top = m_row + 1

            elif target < matrix[m_row][0]:
                bot = m_row - 1
            else:
                break


        if not (top <= bot):
            return False
        m_row  = (top + bot) // 2

        l, r = 0, cols - 1
        while l <= r:
            m = l + (r - l) // 2
            if target > matrix[m_row][m]:
                l = m + 1
            elif target < matrix[m_row][m]:
                r = m - 1
            else:
                return True


        return False


        
        