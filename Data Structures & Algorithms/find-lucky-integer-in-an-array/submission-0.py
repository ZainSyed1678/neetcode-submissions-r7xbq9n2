class Solution:
    def findLucky(self, arr: List[int]) -> int:
        occur = {}
        for i in arr:
            occur[i] = occur.get(i,0) + 1

        ans = -1
        for keys,values in occur.items():
            if keys == values:
                ans =  max(ans,keys)
        return ans
