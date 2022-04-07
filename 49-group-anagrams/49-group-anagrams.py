class Solution:
    def groupAnagrams(self, str: List[str]) -> List[List[str]]:
        hash = {}
        for i in str:
            s = "".join(sorted(i))
            if s not in hash:
                hash[s] = [i]
            else:
                hash[s].append(i)
        return hash.values()