class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hash = {}

        for i in nums:
            num = 0
            temp = i

            for _ in range(len(str(i))):
                num += temp%10
                temp = temp//10

            if num not in hash:
                hash[num] = [i]
            else:
                hash[num].append(i)

        res = -1

        for val in hash:

            if len(hash[val]) > 1:
                arr = hash[val]
                temp = max(arr)
                tempI = arr.index(temp)
                final = 0

                for i in range(len(arr)):
                    if i != tempI:
                        final = max(arr[i]+temp, final)

                res = max(res, final)
        return res