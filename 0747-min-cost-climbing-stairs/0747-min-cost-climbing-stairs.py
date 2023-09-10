class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        res = [-1]*n
        res[0], res[1] = cost[0], cost[1]
        for i in range(2, n):
            res[i] = cost[i] + min(res[i-1], res[i-2])

        return min(res[n-1], res[n-2])
