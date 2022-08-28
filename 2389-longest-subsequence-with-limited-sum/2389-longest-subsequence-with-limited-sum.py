class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        psum = [0]
        for n in nums:
            psum.append(psum[-1] + n)
        ans = []    
        for q in queries:
            ans.append(bisect.bisect_right(psum, q) - 1)
        return ans