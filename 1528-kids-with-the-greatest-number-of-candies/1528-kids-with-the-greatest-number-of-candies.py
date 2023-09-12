class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        cur = 0
        mx = max(candies)

        for kid in candies:
            if kid + extraCandies >= mx:
                cur = kid
                res.append(True)
            else:
                res.append(False)

        return res