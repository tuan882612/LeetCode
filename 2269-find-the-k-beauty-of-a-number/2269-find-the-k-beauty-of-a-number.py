class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nums = str(num)
        res = 0

        for i in range(k, len(nums)+1):
            temp = int(nums[i-k:i])

            if temp != 0:
                if num%temp == 0:
                    res += 1

        return res