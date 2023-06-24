class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): 
            return []

        n = len(p)
        ref, ht = Counter(p), Counter(s[:n])
        res = []

        if ref == ht:
            res.append(0)

        for i in range(len(s)-n):
            ht[s[i]] -= 1
            ht[s[i+n]] += 1

            if ht == ref:
                res.append(i+1)

        return res