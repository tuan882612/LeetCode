class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""
        for i in range(0, min(len(word1), len(word2))):
            new_word += word1[i]
            new_word += word2[i]

        new_word += word1[i+1:]
        new_word += word2[i+1:]

        return new_word