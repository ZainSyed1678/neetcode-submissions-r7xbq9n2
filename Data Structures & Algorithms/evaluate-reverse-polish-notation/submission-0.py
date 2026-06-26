class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        o = "+-*/"
        stack = []
        for i in tokens:
            if i not in o:
                stack.append(int(i))
            if i == "+":
                a = stack.pop()
                b = stack.pop()
                ans = int(a + b)
                stack.append(ans)

            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                ans = int(b - a)
                
                
                stack.append(ans)
            
            elif i == "*":
                a=stack.pop()
                b =stack.pop()
                ans = int(a * b)
                stack.append(ans)


            elif i == "/":
             a = stack.pop()
             b= stack.pop()
             ans = int(b/a)
             stack.append(ans)
        return stack[0]