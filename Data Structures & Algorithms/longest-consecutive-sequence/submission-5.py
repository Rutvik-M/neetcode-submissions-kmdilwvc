class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        longest=0
        for num in nums:
            if (num-1) not in hashset:
                curr_count=1
                curr_num=num
                while (curr_num+1) in hashset:
                    curr_num+=1
                    curr_count+=1
                longest=max(longest,curr_count)
        return longest







        