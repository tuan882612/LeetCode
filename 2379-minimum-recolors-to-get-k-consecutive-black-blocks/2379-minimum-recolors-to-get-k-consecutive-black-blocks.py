class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        ans = 0

        for i in range(len(s) - k + 1):
            ans = max(s.count('B', i, i + k), ans)

        return k - ans