class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {0:1}
        sm = count = 0
        for i in range(len(nums)):
            sm += nums[i]
            if sm-k in hash:
                count+=hash[sm-k]
            if sm not in hash:
                hash[sm] = 1
            else:
                hash[sm] += 1
        return count
            