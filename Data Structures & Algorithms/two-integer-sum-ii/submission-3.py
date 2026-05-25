class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            total=numbers[left]+numbers[right]
            if total==target:
                return [left+1,right+1]
            if total<target:
                left+=1
            else:
                right-=1
numbers = [1,2,3,4]
target = 3
sol=Solution()
res=sol.twoSum(numbers,target)
print(res)


        