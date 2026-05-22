class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li={}
        for i,num in enumerate(nums):
            remain=target-num
            if remain in li:
                return [li[remain],i]
            li[num]=i
        return [-1,-1]
            
        