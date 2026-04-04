class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token=="+":
                stack.append(stack.pop()+stack.pop())
            elif token=="*":
                stack.append(stack.pop()*stack.pop())
            elif token=="-":
                right_num=stack.pop()
                left_num=stack.pop()
                stack.append(left_num-right_num)
            elif token=="/":
                right_num=stack.pop()
                left_num=stack.pop()
                stack.append(int(left_num/right_num))
            else:
                stack.append(int(token))
        return stack[0]

        