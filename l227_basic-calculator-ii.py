class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                tmp = 0
                while i < len(s) and s[i].isdigit():
                    tmp = tmp * 10 + int(s[i])
                    i += 1
                stack.append(tmp)
                # 如果栈中有乘除，先算出来
                while len(stack) > 1 and stack[-2] in {"*", "/"}:
                    stack.pop()
                    opt = stack.pop()
                    if opt == "*":
                        stack.append(stack.pop() * tmp)
                    else:
                        stack.append(stack.pop() // tmp)
            elif s[i] in { "*", "/", "+", "-"}:
                stack.append(s[i])
                i += 1
            else:
                 i += 1
        res = 0
        sign = 1
        for t in stack:
            if t == "+":
                sign = 1
            elif t == "-":
                sign = -1
            else:
                res += sign * t
        return res