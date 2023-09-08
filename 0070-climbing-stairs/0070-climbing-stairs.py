class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        res = [2, 1]

        for i in range(3, n):
            res[i%2] = res[0] + res[1]

        return res[0] + res[1]