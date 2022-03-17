class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        res = left = 0
        for start in range(len(s)):
            if s[start] in hash:
                left = max(left, hash[s[start]]+1)
            hash[s[start]] = start
            res = max(res, start-left+1)
        return res