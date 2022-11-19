import collections

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hash = defaultdict(int)
        res = 0 
        
        for i in time:
            if i%60 == 0:
                res += hash[0]
            else:
                res += hash[60-(i%60)]
            hash[i%60] += 1
            
        return res