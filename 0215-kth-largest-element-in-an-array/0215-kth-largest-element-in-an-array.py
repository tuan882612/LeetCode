class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return [heapq.heappop(nums) for i in range(len(nums))][len(nums)-k]
