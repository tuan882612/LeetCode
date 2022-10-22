import heapq

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        res = 0
        temp = []
        
        for _ in range(len(nums)):
            temp.append(heapq.heappop(nums))
            
            if len(temp) > 1:
                res += min(temp)
                temp = []
            
        return res