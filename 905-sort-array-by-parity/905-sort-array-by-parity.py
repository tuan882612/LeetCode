class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr = []
        evens = 0
        for i in nums:
            if i%2 == 0:
                arr.insert(evens, i)
                evens += 1
            else:
                arr.append(i)
                
        return arr
        