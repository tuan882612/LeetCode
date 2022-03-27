class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hash = {}
        for i, v in enumerate(mat):
            hash[i] = v.count(1)
        arr = sorted(hash.items(), key = lambda x:x[1])[:k]
        return [i[0] for i in arr]