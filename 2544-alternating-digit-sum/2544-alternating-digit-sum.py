class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = int(str(n)[::-1])
        div = 1
        res = 0

        while n > 0:
            temp = n%10*div
            div *= -1
            res += temp
            n = n//10

        return res
        