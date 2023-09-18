class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in "".join(s+s)[1:-1]
