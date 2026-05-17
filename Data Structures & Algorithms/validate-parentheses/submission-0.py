class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:

            # opening bracket
            if c in "([{":
                stack.append(c)

            # closing bracket
            else:

                # stack empty OR wrong bracket
                if not stack or stack[-1] != pairs[c]:
                    return False

                stack.pop()

        return len(stack) == 0