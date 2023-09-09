class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        print("".join(s+s)[1:-1])
        return s in "".join(s+s)[1:-1]
