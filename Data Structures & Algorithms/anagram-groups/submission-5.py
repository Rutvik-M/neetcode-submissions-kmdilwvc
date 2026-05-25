class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequency={}
        for word in strs:
            count=[0]*26
            for ch in word:
                count[ord(ch)-ord('a')]+=1
            key=tuple(count)
            if key not in frequency:
                frequency[key]=[]
            frequency[key].append(word)
        return list(frequency.values())
        