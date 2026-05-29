class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
         return 0
 #via sorting method 
        nums.sort()

        curr = 1
        maxi = 1

        for i in range(1, len(nums)):
 
         if nums[i] == nums[i-1]:
            continue

         elif nums[i] == nums[i-1] + 1:

            curr += 1
 
         else:

            maxi = max(maxi, curr)

            curr = 1

        return max(maxi, curr)
        #complexity will be O(n logn) because of sorting