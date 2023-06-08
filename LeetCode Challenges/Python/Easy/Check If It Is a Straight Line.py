"""You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
Source: https://leetcode.com/problems/check-if-it-is-a-straight-line/"""

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        if x1 - x0 == 0:
            for i in range(2, len(coordinates)):
                x, y = coordinates[i]
                if x - x0 != 0:
                    return False
        else:
            slope = (y1 - y0) / (x1 - x0)
            for i in range(2, len(coordinates)):
                x, y = coordinates[i]
                if x - x0 == 0 or (y - y0) / (x - x0) != slope:
                    return False
        
        return True
