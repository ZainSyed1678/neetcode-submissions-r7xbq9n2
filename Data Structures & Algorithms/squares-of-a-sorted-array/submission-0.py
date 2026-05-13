class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for num in range(len(nums)):
            nums[num] = nums[num] ** 2
            
        return sorted(nums)    