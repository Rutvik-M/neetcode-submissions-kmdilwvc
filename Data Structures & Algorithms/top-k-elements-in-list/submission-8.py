class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        ans=[[]for _ in range(len(nums)+1)]
        res=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num,c in freq.items():
            ans[c].append(num)
        for i in range(len(ans)-1,0,-1):
            for num in ans[i]:
                res.append(num)
            if len(res)==k:
                return res


        