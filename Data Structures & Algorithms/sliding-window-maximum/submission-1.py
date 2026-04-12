class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result=[]
        left=0
        for right in range(len(nums)):
            if (right-left+1) ==k:
                curr_window=nums[left : right+1]
                max_window=max(curr_window)
                result.append(max_window)
                left+=1
        return result
        