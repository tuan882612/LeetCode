class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n):
            if n in dp:
                return dp[n]

            dp[n] = helper(n-1) + helper(n-2)
            return dp[n]

        dp = {1: 1, 2: 2}
        return helper(n)
        