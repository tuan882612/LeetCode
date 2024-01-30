class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n1 = n2 = 0

        for i in range(len(s)):
            n1 += ord(s[i])
            n2 += ord(t[i])

        return chr((n2 + ord(t[len(t)-1])) - n1)