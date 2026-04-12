class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(s)<len(t):
            return ""
        hashmap1={}
        for i in t:
            hashmap1[i]=hashmap1.get(i,0)+1
        hashmap2,left,res,res_len,have,need={},0,[-1,-1],float('infinity'),0,len(hashmap1)
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


        