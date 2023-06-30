class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = [(-v, k) for k, v in Counter(words).items()]
        heapq.heapify(res)
        return [heapq.heappop(res)[1] for _ in range(k)]