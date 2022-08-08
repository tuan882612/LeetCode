class Solution:
    def findSum(self,n):
        total=0
        while n!=0:
            total=total+(n%10)
            n=n//10
        return total
    def maximumSum(self, nums: List[int]) -> int:
        maps={}
        ans=-1
        for n in nums:
            key=self.findSum(n)
            if key in maps:
                maps[key].append(n)
            else:
                maps[key]=[n]
        for key in maps:
            if len(maps[key])>=2:
                maps[key].sort()
                ans=max(ans,maps[key][-1]+maps[key][-2])
        return ans