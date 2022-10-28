class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        
        for i in strs:
            temp = "".join(sorted(i))
            if temp not in hash:
                hash[temp] = [i]
            else:
                hash[temp].append(i)
                
        return hash.values()