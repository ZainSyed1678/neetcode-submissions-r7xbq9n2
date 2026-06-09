class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        times = {}
        for num in nums:
            times[num] = times.get(num,0) + 1
        for num in times:
            if times[num] > len(nums) // 2:
                return num