class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c1, c2 = cost[0], cost[1]

        for c in cost[2:]:
            c1, c2 = c2, min(c1, c2) + c

        return min(c1, c2)