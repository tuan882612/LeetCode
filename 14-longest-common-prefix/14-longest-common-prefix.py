class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cmp = max(strs)
        for i, c in enumerate(min(strs)):
            if c != cmp[i]:
                return cmp[:i]
        return min(strs)