class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        psum = [0]
        
        for n in nums:
            psum.append(psum[-1] + n)

        return [bisect.bisect_right(psum, i) - 1 for i in queries]