class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])

        for i in range(2, n):
            cost[i] += min(cost[i-1], cost[i-2])

        return min(cost[n-1], cost[n-2])