class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        n = len(nums)
        for i in range(n):
            if nums[i] == key:
                for x in range(max(i-k, 0), min(i+k, n-1)+1):
                    res.add(x)

        return list(res)