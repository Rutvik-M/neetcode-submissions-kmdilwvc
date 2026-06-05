class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
      
        for words in strs:
            word=[0]*26
            for ch in words:
                word[ord(ch)-ord("a")]+=1
            tup=tuple(word)
            if tup not in ans:
                ans[tup]=[]
            ans[tup].append(words)
        return list(ans.values())

            

        