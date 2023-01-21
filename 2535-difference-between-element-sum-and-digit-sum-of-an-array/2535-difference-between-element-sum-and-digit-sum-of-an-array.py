class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        pre = 0
        post = 0
        
        for i in nums:
            pre += i
            post += self.func(i)

        return pre-post

    def func(self, num: int) -> int:
        n = list(str(num))
        sm = 0

        for i in n:
            sm += int(i)

        return sm