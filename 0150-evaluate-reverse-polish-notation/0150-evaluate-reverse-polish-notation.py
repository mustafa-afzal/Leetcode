class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = int(tokens[0])
        for i in range(len(tokens)):
            if tokens[i] == "+":
                res = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif tokens[i] == "-":
                res = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif tokens[i] == "*":
                res = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif tokens[i] == "/":
                res = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return res
