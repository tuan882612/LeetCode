class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = {}
        res, l = 0, 0

        for idx, r in enumerate(s):
            if r in ht and ht[r] >= l:
                l = ht[r] + 1
            else:
                res = max(res, idx-l + 1)
                
            ht[r] = idx

        return res