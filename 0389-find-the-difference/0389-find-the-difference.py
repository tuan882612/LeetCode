class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ht = Counter(s)
        htR = Counter(t)

        for k, v in htR.items():
            if ht[k] != v:
                return k

        return ""