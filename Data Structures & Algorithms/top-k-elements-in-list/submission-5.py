class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result,hashmap,freq=[],{},[[] for i in range(len(nums)+1)]
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        for num,i in hashmap.items():
            freq[i].append(num)
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                result.append(num)
                if len(result)==k:
                    return result

        