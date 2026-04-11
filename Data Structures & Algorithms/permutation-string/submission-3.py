class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        hashmap1={}
        for i in s1:
            hashmap1[i]=hashmap1.get(i,0)+1
        hashmap2={}
        left=0
        for right in range(len(s2)):
            char_in=s2[right]
            hashmap2[char_in]=hashmap2.get(char_in,0)+1

            if right-left+1>len(s1):
                char_out=s2[left]
                hashmap2[char_out]-=1
                if hashmap2[char_out]==0:
                    del hashmap2[char_out]
                left+=1
            if hashmap2==hashmap1:
                return True
        return False
        



        