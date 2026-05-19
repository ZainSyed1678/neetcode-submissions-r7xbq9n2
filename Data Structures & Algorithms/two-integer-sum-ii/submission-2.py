class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        cal = 0
        while low < high:
            cal = numbers[low] + numbers[high]
            if cal < target:
                low += 1
            elif cal > target:
                high -= 1
            else:
                return [low+1,high+1]