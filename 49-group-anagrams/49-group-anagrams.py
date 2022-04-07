class Solution:
    def groupAnagrams(self, str: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for i in str:
            count = [0]*26
            for c in i:
                count[ord(c) - ord("a")] += 1
            hash[tuple(count)].append(i)
        return hash.values()