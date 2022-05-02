from collections import deque
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr = deque()
        
        for i in nums:
            if i%2 == 0:
                arr.appendleft(i)
            else:
                arr.append(i)
                
        return arr
        