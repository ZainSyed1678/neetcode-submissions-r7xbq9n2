class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(2):
            for num in nums:
                answer.append(num)
        return answer