class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        hash = sorted(hash.items(), key = lambda x:x[1], reverse = True)[:k]
        return [i[0] for i in hash]