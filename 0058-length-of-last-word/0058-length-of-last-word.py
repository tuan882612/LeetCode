class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for ch in reversed(s.strip()):
            if ch == " ":
                return res
            res += 1
        return res