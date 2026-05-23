class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        
        for word in strs:
            count=[0]*26
            for char in word:
                count[ord(char)-ord("a")] = count[ord(char)-ord("a")]+1
            sign=tuple(count)
            if sign not in hashmap:
                hashmap[sign]=[]
            hashmap[sign].append(word)
        return list(hashmap.values())

   

        # TC = O(n*k)--> n because n words there and k because nested loop len(word) time only
        # SC = O(n)--> because we are storing all characters with counting atleast 1 time in hashmap
        