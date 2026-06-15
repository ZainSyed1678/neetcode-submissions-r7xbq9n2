class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        max_sum = float("-inf")
        res = []
        for r in range(len(nums)):
    

            if r - l + 1 > k:
                l += 1
            if r - l + 1 == k:
               win_max = max(nums[l:r+1])
               res.append(win_max)
        return res
