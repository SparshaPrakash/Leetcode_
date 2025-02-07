from typing import List
import math

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def calcDist(p1: List[int], p2: List[int]) -> float:
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        distances = set()
        
        distances.add(calcDist(p1, p2))
        distances.add(calcDist(p2, p3))
        distances.add(calcDist(p3, p4))
        distances.add(calcDist(p1, p3))
        distances.add(calcDist(p1, p4))
        distances.add(calcDist(p2, p4))

        return 0.0 not in distances and len(distances) == 2

        