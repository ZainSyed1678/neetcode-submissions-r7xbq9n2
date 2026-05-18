class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for i in operations:
            
            if i == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
            elif i == "C":
                stack.pop(-1)
            elif i == "D":
               d = stack[-1] * 2
               stack.append(d)
            else:
                stack.append(int(i)) # for converting string into integer and directly push them into stack
        return sum(stack)
