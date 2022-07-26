class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hash = {}
        pair = 0
        one = 0

        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1

        for i in hash.values():
            if i%2 == 0:
                pair += i//2
            else:
                if i > 1:
                    pair += i//2
                one += 1

        return [pair, one]
