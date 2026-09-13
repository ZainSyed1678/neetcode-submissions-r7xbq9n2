class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        n  = len(nums)
        ans = 0
        z = 0
        for r in range(n):
            if nums[r] == 0:
                z += 1
            while z > k:
                if nums[l] == 0:
                    z -= 1
                l += 1
            ans = max(ans,r-l+1)
        return ans