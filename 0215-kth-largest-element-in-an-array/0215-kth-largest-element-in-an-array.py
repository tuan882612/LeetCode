class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        arr = [heapq.heappop(nums) for i in range(len(nums))]
        return arr[len(nums)-k]