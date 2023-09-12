class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ht = defaultdict(list)
        res = []

        for i, v in enumerate(groupSizes):
            ht[v].append(i)

            if len(ht[v]) == v:
                res.append(ht[v])
                del ht[v]

        return res