class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        # we iterate from the end lleaving the goal index and check if from that position we can reach the goal
        for i in range(len(nums) -2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
        