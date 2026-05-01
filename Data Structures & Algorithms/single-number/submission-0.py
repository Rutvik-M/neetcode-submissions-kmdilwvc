class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap={}
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        for i in hashmap:
            if hashmap[i]==1:
                return i
        