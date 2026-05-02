class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        exp=(n*(n+1))//2
        actual_sum=sum(nums)
        return exp-actual_sum