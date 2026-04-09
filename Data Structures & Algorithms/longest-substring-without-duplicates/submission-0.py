class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_length=0
        hashmap={}
        for right in range(len(s)):
            curr_char=s[right]
            if curr_char in hashmap and hashmap[curr_char]>=left:
                left=hashmap[curr_char]+1
            curr_length=right-left+1
            max_length=max(max_length,curr_length)
            hashmap[curr_char]=right
        return max_length


        