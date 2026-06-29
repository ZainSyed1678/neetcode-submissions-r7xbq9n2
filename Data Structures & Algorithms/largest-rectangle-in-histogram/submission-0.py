class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        big = 0
        stack = []
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h= heights[stack.pop()]
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                big = max(big,h * w)
            stack.append(i)
        return big