class Solution:
    def groupAnagrams(self, str: List[str]) -> List[List[str]]:
        hash = {}
        for i in str:
            q = "".join(sorted(i))
            if q not in hash:
                hash[q] = [i]
            else:
                hash[q].append(i)
        return [i for i in hash.values()]