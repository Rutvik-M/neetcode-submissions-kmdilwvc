class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token=="+":
                right_no=stack.pop()
                left_no=stack.pop()
                stack.append(left_no+right_no)
            elif token=="-":
                right_no=stack.pop()
                left_no=stack.pop()
                stack.append(left_no-right_no)
            elif token=="*":
                right_no=stack.pop()
                left_no=stack.pop()
                stack.append(left_no*right_no)
            elif token=="/":
                right_no=stack.pop()
                left_no=stack.pop()
                stack.append(int(left_no / right_no))
            else:
                stack.append(int(token))
        return stack[0]
        