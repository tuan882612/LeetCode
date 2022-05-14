class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = 0

        for i in range(1, len(sequence)+1):

            if word*i in sequence:
                res += 1
            else:
                break

        return res