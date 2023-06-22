class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) < 2:
            return 1

        res = l = 0
        ht = {}

        for r in range(len(fruits)):
            if fruits[r] not in ht:
                ht[fruits[r]] = 1
            else:
                ht[fruits[r]] += 1

            while len(ht) > 2:
                ht[fruits[l]] -= 1
                if ht[fruits[l]] == 0:
                    del ht[fruits[l]]
                l += 1

            res = max(res, r-l+1)
        return res