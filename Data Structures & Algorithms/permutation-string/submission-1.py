class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        fa = {}
        
        for c in s1:
            fa[c] = fa.get(c,0) + 1
        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                l += 1
            if r - l + 1 == len(s1):
                win_freq = {}
                for c in s2[l:r+1]:
                  win_freq[c] = win_freq.get(c, 0) + 1
                if fa == win_freq:
                    return True
                
        return False