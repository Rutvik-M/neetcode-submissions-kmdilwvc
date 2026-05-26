class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=[1]*len(nums)
        pre=1
        for i in range(len(nums)):
            n[i]=pre
            pre=pre*nums[i]
        post=1
        for i in range(len(nums)-1,-1,-1):
            n[i]=n[i]*post
            post=post*nums[i]
        return n
            
            
            



        