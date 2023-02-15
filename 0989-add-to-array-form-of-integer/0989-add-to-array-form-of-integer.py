class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = int("".join(str(i) for i in num))
        return list(map(int, list(str(n+k))))