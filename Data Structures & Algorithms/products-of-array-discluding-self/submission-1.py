class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Brute force 
        result = [0] * len(nums)
        for i in range(len(nums)):
            mul = 1 
            for j in range(len(nums)):
                if i == j:
                    continue
                mul *= nums[j]
            result[i] = mul
        return result