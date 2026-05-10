class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            key = [0] * 26 # for each alphabet 
            for c in s:
                key[ord(c) - ord('a')] += 1 # ascii - a so we get the value of the alphabet

            key = tuple(key) # list cannot be keys thats why

            ans[key].append(s) # appending sinces its a list
        return list(ans.values())