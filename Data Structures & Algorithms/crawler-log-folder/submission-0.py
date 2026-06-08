class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        stack = []
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log != "./":
                stack.append(log)
        return len(stack)

