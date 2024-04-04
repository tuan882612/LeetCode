class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)

        for i in range(n, len(haystack)+1):
            idx = i-n
            if haystack[idx:i] == needle:
                return idx

        return -1