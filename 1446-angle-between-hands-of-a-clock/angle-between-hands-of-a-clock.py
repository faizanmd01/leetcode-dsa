class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        diff=abs(60*(hour%12)-11*minutes)*0.5
        return min(diff,360-diff)
        