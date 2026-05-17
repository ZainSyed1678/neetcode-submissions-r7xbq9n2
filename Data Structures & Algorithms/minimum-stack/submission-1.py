class MinStack:

    def __init__(self):
        
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
         tempo = []
         minimum = self.stack[-1]

         while len(self.stack):
            minimum = min(minimum, self.stack[-1])
            tempo.append(self.stack.pop())

         while len(tempo):
            self.stack.append(tempo.pop())

         return minimum
         # O(1) complexity condition gets satisifed
