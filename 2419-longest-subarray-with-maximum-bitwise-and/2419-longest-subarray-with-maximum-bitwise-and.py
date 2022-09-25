class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi=max(nums)
        len1=0
        curr=0
        for i in nums:
            if i==maxi:
                curr+=1
            else:
                len1=max(len1,curr)
                curr=0
        len1=max(curr,len1)
        return len1