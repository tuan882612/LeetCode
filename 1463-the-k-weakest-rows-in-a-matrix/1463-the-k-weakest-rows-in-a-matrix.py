class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ht = {i:r.count(1) for i, r in enumerate(mat)}
        return [i[0] for i in sorted(ht.items(), key=lambda x:x[1])[:k]]