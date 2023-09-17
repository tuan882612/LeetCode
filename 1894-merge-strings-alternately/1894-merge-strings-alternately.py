class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for l1, l2 in zip_longest(word1, word2):
            if l1 and l2:
                res = "".join(res + l1 + l2)
            elif not l1:
                res = "".join(res + l2)
            else:
                res = "".join(res + l1)

        return res