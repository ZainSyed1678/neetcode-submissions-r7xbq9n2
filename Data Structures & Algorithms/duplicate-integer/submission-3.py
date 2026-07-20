class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = []
        for n in nums:
            if n not in new:
                new.append(n)
        if new != nums:
            return True
        else:
            return False