class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for word in strs:
            frequency=[0]*26
            for ch in word:
                frequency[ord(ch)-ord('a')]+=1
            words=tuple(frequency)
            if words not in hashmap:
                hashmap[words]=[]
            hashmap[words].append(word)
        return list(hashmap.values())
        