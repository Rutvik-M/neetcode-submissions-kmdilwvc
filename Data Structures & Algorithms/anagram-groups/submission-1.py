class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for word in strs:
            alphas=[0]*26
            for ch in word:
                alphas[ord(ch) - ord('a')]=alphas[ord(ch) - ord('a')]+1
            sign=tuple(alphas)
            if sign not in freq:
                freq[sign]=[]
            freq[sign].append(word)
        return list(freq.values())

        