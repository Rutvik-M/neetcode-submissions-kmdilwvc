class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        block=len(s1)
        hashmap1={}
        for i in s1:
            hashmap1[i]=hashmap1.get(i,0)+1
        for i in range(len(s2)):
            block2=s2[i:i+block]
            if Counter(block2) == hashmap1:
                return True

            
        return False



        