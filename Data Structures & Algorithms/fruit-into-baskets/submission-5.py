class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        ans = 0
        freq = {}
        k = 2
        for r in range(n):
            x = arr[r]
            freq[x] = freq.get(x,0) + 1
            while len(freq) > k:
                y = arr[l]
                freq[y] -= 1
                if freq[y] == 0:
                    del freq[y]
                l +=1
            ans = max(ans,r-l+1)
        return ans 
