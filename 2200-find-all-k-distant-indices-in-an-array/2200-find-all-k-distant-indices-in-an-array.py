class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        index = [i for i in range(len(nums)) if nums[i] == key]
        res = set()
        for i in range(len(nums)):
            for j in index:
                if abs(i-j) <= k:
                    res.add(i)
        return res