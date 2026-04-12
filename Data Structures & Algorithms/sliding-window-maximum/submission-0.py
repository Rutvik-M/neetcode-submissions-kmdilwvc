class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        res=[]
        for right in range(len(nums)):
            if (right-left+1)==k:
                curr_window=nums[left : right+1]
                curr_max=max(curr_window)
                res.append(curr_max)
                left+=1
        return res
        