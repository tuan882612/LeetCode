class Solution:
    def search(self, nums: List[int], target: int) -> int:
        z = list(zip(nums, [i for i in range(len(nums))]))
        for i, n in z:
            if i == target:
                return n
        return -1