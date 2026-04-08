class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        best_speed=right
        while left <= right:
            mid=(left+right)//2
            hours_taken=0
            for pile in piles:
                hours_taken=hours_taken + math.ceil(pile/mid)
            if hours_taken <=h:
                best_speed=mid
                right=mid-1
            else:
                left=mid+1
        return best_speed

                
        