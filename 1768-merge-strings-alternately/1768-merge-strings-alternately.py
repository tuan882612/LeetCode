class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        if not word2:
            return word1

        res = ""
        if len(word1) <= len(word2):
            shortest = word1
            longest = word2
            shortest_len = len(word1)
            diff = abs(len(word2) - len(word1))

        else:
            shortest= word2
            longest = word1
            shortest_len = len(word2)
            diff = abs(len(word2)- len(word1))


        for i in range(shortest_len):
            res += word1[i]
            res += word2[i]

        return res + longest[shortest_len: shortest_len + diff]
