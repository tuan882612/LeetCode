class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = collections.defaultdict(list)
        
        for i in strs:
            hash[frozenset(collections.Counter(i).items())].append(i)
        
        return hash.values()