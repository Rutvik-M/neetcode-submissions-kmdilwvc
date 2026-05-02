class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647  # 2^31 - 1
        
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            # 1. Pop the last digit
            digit = x % 10
            
            # 2. Check for 32-bit overflow BEFORE we push the digit!
            # If res is exactly INT_MAX // 10, the next digit cannot be greater than 7
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return 0
                
            # 3. Push the digit onto our result
            res = (res * 10) + digit
            
            # 4. Shrink x
            x = x // 10
            
        return res * sign