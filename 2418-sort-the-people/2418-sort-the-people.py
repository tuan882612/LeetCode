class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ref = [(i,j) for i, j in zip(names, heights)]
        ref = list(sorted(ref, key=lambda x:x[1], reverse=True))
        return [i for i, j in ref]