class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            tot =numbers[left] + numbers[right]
            if tot == target:
                return [left +1, right + 1]
            if tot > target:
                right -= 1
            if tot < target:
                left += 1

