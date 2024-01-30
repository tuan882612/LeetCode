class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(ord(c) for c in t) - sum(ord(c) for c in s))