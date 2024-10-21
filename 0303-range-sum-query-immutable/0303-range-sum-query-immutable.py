from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        for i in range(self.n):
            self._update(i + 1, nums[i])

    def _update(self, i: int, delta: int):
        while i <= self.n:
            self.tree[i] += delta
            i += (i & -i)

    def _prefix_sum(self, i: int) -> int:
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= (i & -i)
        return total

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sum(right + 1) - self._prefix_sum(left)
