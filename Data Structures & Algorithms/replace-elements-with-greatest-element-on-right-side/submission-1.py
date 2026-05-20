class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        resu = [0] * n 
        for i in range(len(arr)):
            high = -1
            for j in range(i+1,n):
                high = max(high,arr[j])
            resu[i] = high
        return resu

