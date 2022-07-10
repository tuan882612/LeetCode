class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join([str(i) for i in digits])
        return [int(i) for i in str(int(num)+1)]