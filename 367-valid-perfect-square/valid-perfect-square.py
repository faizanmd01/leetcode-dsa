class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1:
            return False
            
        # Start our guess at num // 2 (or num itself for small numbers)
        r = num
        while r * r > num:
            r = (r + num // r) // 2
            
        return r * r == num