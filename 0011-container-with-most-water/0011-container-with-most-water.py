class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        left, right = 0, len(height) - 1

        while left < right:
            min_height = min(height[left], height[right])
            area = min_height * (right - left)
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        max_area = 0

        left, right = 0, len(height) - 1

        while left < right:
            min_height = min(height[left], height[right])
            area = min_height * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area