class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxy = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            maxy  = max(maxy,curr)
        return maxy