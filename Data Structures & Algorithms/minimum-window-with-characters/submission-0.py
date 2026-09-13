class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        have = {}
        need = {}
        for c in t:
            need[c] = need.get(c,0) + 1
        formed = 0
        ans = ""
        required = len(need)
        for r in range(len(s)):
            c = s[r]
            have[c] = have.get(c,0) + 1
            if c in need and have[c] == need[c]:
                formed += 1
            while formed == required:
                if ans == "" or r - l + 1 < len(ans):
                    ans = s[l:r+1]
                left = s[l]
                have[left] -= 1
                if left in need and have[left] < need[left]:
                    formed -= 1
                l += 1
        return ans