class Solution:
    def nonchar(self,ch):
        return (
            ord('A')<=ord(ch)<=ord('Z') or
            ord('a')<=ord(ch)<=ord('z') or
            ord('0')<=ord(ch)<=ord('9')
            )
    def isPalindrome(self, s: str) -> bool:

        first,last=0,len(s)-1
        while first<last:
            while first<last and not self.nonchar(s[first]):
                first+=1
            while first<last and not self.nonchar(s[last]):
                last-=1
            if s[first].lower()!=s[last].lower():
                return False
            first+=1
            last-=1
        return True