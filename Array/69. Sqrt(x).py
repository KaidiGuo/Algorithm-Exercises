# BINARY SEARCH

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left<=right:
            middle = left + int((right-left)/2)
            if middle ** 2 == x:
                return middle
            elif middle ** 2 > x and (middle-1)**2 < x:
                return middle -1
            elif middle** 2 < x:
                left = middle + 1
            elif middle **2 > x:
                right = middle -1
        return left