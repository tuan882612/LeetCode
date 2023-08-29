from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for dil in "!?',;. ":
            paragraph = "-".join(paragraph.split(dil))

        ht = defaultdict(int)
        res, mx = '', 0

        for word in paragraph.lower().split("-"):
            if word in banned or not word: 
                continue
            ht[word] += 1
            if ht[word] > mx:
                mx = ht[word]
                res = word

        return res