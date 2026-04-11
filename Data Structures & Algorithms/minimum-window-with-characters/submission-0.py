class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t)>len(s):
            return ""
        hashmap1={}
        for char in t:
            hashmap1[char]=hashmap1.get(char,0)+1
        hashmap2={}
        have=0
        need=len(hashmap1)
        res=[-1,-1]
        res_len=float("infinity")
        left=0
        for right in range(len(s)):
            char_in=s[right]
            hashmap2[char_in]=hashmap2.get(char_in,0)+1
            if char_in in hashmap1 and hashmap2[char_in]==hashmap1[char_in]:
                have+=1
            while have==need:
                if (right-left+1)<res_len:
                    res=[left,right]
                    res_len=right-left+1
                char_out=s[left]
                hashmap2[char_out]-=1
                if char_out in hashmap1 and hashmap2[char_out]<hashmap1[char_out]:
                    have-=1
                left+=1
        left_index,right_index=res
        return s[left_index : right_index+1] if res_len != float("infinity") else ""
        