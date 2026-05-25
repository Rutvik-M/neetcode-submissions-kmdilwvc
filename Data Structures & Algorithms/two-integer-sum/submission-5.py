class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,num in enumerate(nums):
            remain=target-num
            if remain in hashmap:
                return [hashmap[remain],i]
            hashmap[num]=i
        return [-1,-1]

nums = [3,4,5,6]
target = 7
sol=Solution()
result=sol.twoSum(nums,target)
print(result)