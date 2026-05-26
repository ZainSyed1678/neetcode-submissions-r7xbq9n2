class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        seen = set(nums)

        i = 1

        while True:

            if i not in seen:

                return i

            i += 1