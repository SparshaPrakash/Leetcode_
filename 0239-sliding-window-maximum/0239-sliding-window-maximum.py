class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # to store the index
        l = r = 0

        while r < len(nums):
            # pop smaller vlaues from q
            while  q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left value from the window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output
    
        