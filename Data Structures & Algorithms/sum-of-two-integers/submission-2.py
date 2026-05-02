class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xffffffff
        while (b & mask)>0:
            carry=(a&b)<<1
            a=a^b
            b=carry
        a = a & mask
        if a <= 0x7fffffff:
            return a
        else:
            return ~(a^mask)
    
        