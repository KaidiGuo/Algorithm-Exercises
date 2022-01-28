# BINARY SEARCH

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left<=right:
            middle = left + int((right-left)/2)
            if middle ** 2 == num:
                return True
            elif middle ** 2 >num:
                right = middle -1
            elif middle ** 2 <num:
                left = middle +1
        return False

    