import heapq

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        res = 0
        temp = []
        
        while nums:
            n = heapq.heappop(nums)
            temp.append(n)
            
            if len(temp) > 1:
                res += min(temp)
                temp = []
            
        return res