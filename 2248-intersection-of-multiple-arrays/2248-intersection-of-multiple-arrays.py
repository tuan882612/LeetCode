class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res=[]
        arr=[]
        n=len(nums)
        for num in nums:
            arr.extend(num)
        count=Counter(arr)
        for i in count:
            if(count[i]==n):
                res.append(i)
        return sorted(res) if res else res