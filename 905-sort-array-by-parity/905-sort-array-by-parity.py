class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr, arr1 = [], []
        for i in nums:
            if i%2 == 0:
                arr.append(i)
                
        for i in nums:
            if i%2 != 0:
                arr1.append(i)
                
        return arr + arr1
                
        