class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])

        preRow1, preRow2 = grid[0].copy(), grid[1].copy() # calculating prefixes for ecah row

        for i in range(1, N):
            preRow1[i] += preRow1[i - 1]  
            preRow2[i] += preRow2[i - 1]  

        res = float("inf")
        for i in range(N): # the index where the first robot h=chnages its direction to move down
            top = preRow1[-1] - preRow1[i]  # getting the total value after the ith index in the top row to see how mcuh robot 2 can collect from the top reminining cilumns
            bottom = preRow2[i - 1] if i > 0 else 0
            secondRobot = max(top, bottom)
            res = min(res, secondRobot) # this is because robot 1 wants to minimize what robot 2 can collect
        return res