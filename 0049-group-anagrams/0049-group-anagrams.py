class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        hash = collections.defaultdict(list)
        
        for i in strs:
            hash[''.join(sorted(i))].append(i)
            
        return hash.values()