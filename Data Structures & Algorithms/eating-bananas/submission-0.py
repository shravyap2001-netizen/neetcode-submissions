class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        low = 1
        high = max(piles)
        def can(k):
            hours = 0 
            for pile in piles: 
                hours += (pile + k - 1) // k 
            return hours <= h
        while low < high:
            mid = low + (high - low)//2
            if can(mid):
                high = mid
            else:
                low = mid + 1

        return low