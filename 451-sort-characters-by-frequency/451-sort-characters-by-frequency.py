class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(k * v for k, v in sorted(Counter(s).items(), key=lambda x : x[1], reverse=True))