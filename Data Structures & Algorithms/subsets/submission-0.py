class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(path,index):
         if index == len(nums):
            ans.append(path.copy())
            return 
         path.append(nums[index])
         backtrack(path, index + 1)
         path.pop()
         backtrack(path,index+ 1)        
        backtrack([],0)
        return ans


        