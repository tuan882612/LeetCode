class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs, ht = Counter(s), Counter(t)
        return hs == ht