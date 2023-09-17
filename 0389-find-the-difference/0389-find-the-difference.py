class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ht = Counter(s)
        htR = Counter(t)

        for i in t:
            if i not in ht or ht[i] != htR[i]:
                return i

        return ""