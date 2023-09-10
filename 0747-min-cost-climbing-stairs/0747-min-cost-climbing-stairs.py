class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c1, c2 = cost[0], cost[1]
        res = min(c1, c2)

        for i in range(2, len(cost)):
            res = cost[i]+min(c1, c2)
            c1 = c2
            c2 = res

        return min(c1, c2)
