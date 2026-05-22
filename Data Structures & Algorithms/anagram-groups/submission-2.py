class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for word in strs:
            count=[0]*26
            for ch in word:
                count[ord(ch)-ord("a")]=count[ord(ch)-ord("a")]+1
            sign=tuple(count)
            if sign not in hashmap:
                hashmap[sign]=[]
            hashmap[sign].append(word)
        return list(hashmap.values())
        