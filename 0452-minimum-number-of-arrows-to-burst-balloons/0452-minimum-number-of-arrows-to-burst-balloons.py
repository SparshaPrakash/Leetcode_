class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        res = len(points)  # initailizing the cout to be the number of intervals 
        prev = points[0] # string the previous interval
        for i in range(1, len(points)):
            curr = points[i]

            if curr[0] <= prev[1]: # checking for overlapping intervals
                res -= 1 
                prev = [curr[0], min(curr[1], prev[1])]  # merging the 2 overlapping inetrbals -> only yhe overlapping part
            else:  # non overlapping intervals
                prev = curr

        return res

        