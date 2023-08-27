class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = {}
        res = l = 0

        for r, letter in enumerate(s):
            if letter in ht:
                l = max(l, ht[letter]+1)

            ht[letter] = r
            res = max(res, r-l+1)
            
        return res