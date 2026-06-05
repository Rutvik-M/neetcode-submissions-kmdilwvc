class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for word in strs:
            count=[0]*26
            for ch in word:
                count[ord(ch)-ord("a")]+=1
            tup=tuple(count)
            if tup not in ans:
                ans[tup]=[]
            ans[tup].append(word)
        return list(ans.values())
        
        