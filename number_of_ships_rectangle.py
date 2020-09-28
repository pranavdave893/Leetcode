"""
https://leetcode.com/problems/number-of-ships-in-a-rectangle/
"""
from __future__ import annotations
class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
       pass


class Point(object):
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        X = topRight.x - bottomLeft.x
        Y = topRight.y - bottomLeft.y

        if X == Y == 0:
            return 
        
        if not sea.hasShips:
            return 0
        
        if X > Y:
            
            half = bottomLeft.x + X // 2

            new_bottom_left = Point(half + 1, bottomLeft.y)
            new_top_right = Point(half topRight.y)

            return self.countShips(sea, topRight, new_bottom_left) + self.countShips(sea, new_top_right, bottomLeft)
        
        else:

            half = bottomLeft.y + Y // 2

            half_bottom_left = Point(bottomLeft.x, half + 1)
            half_top_right = Point(topRight.x, half)

            return self.countShips(sea, half_top_right, bottomLeft) + self.countShips(sea, topRight, half_bottom_left)