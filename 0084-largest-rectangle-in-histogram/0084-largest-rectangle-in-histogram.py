class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # will store indices of bars
        max_area = 0

        # Go through all bars, and one extra step for cleanup
        for i in range(len(heights) + 1):
            # For the last step, use height 0 to flush out remaining bars
            curr_height = heights[i] if i < len(heights) else 0

            # If current bar is lower than the last one in stack
            while stack and curr_height < heights[stack[-1]]:
                h = heights[stack.pop()]          # height of bar
                # width: if stack empty, means h extends from 0 to i-1
                width = i if not stack else (i - stack[-1] - 1)
                max_area = max(max_area, h * width)

            stack.append(i)  # push current index

        return max_area
        