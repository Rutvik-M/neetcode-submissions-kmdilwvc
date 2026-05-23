class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        hashmap={}
        freq=[[] for _ in range(len(nums)+1)]
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1

        for num,i in hashmap.items():
            freq[i].append(num)

        for n in range(len(freq)-1,0,-1):
            for i in freq[n]:
                res.append(i)
                if len(res)==k:

                    return res

        