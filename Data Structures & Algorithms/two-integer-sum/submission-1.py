class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        left=0
        right=len(nums)-1
        ans={}
        for i,num in enumerate(nums):
            remaining=target-num
            if remaining in ans:
                return [ans[remaining],i]
            ans[num]=i
        return [-1,-1]

        