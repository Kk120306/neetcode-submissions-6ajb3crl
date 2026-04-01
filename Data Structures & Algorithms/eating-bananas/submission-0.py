class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)

        while left <= right: 
            mid = left + ((right-left) // 2)
            cnt = 0
            for p in piles: 
                cnt += math.ceil(float(p) / mid)
            if cnt <= h:
                res = mid
                right = mid -1
            else :
                left = mid + 1
        return res
