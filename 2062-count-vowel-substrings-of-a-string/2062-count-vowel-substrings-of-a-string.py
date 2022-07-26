class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        res = 0
        k = -1
        vowels = {'a', 'e', 'i', 'o', 'u'}
        hash = {vowel: -1 for vowel in vowels}

        for i, char in enumerate(word):
            if char not in vowels:
                k = i
            else:
                hash[char] = i
                res += max(min(hash.values()) - k, 0)
        return res
