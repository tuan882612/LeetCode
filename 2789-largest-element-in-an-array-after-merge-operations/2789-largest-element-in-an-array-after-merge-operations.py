class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        stack = []
        
        for i in reversed(nums):
            while stack and stack[-1] >= i:
                 i += stack.pop()
            stack.append(i)

        return stack[-1]