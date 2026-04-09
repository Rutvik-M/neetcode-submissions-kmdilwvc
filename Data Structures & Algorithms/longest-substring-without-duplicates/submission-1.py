class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_len=0
        hashmap={}
        for i in range(len(s)):
            char=s[i]
            if char in hashmap and hashmap[char]>=left:
                left=hashmap[char]+1
            curr_len=i-left+1
            max_len=max(curr_len,max_len)
            hashmap[char]=i
        return max_len
        