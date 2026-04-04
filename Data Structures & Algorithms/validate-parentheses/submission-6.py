class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={")":"(","]":"[","}":"{"}
        stack=[]
        for i in s:
                if i in hashmap:
                        top=stack.pop() if stack else 0
                        if hashmap[i]!=top:
                            return False
                else:
                    stack.append(i)
        return len(stack)==0
                        
        