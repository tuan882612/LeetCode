import collections

class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        unique = min(len(set(s)), len(s) // count)
        hash = collections.Counter()
        res = 0 
        
        for i in range(1, unique + 1):
            size = count * i
            temp_count = 0

            for j, a in enumerate(s):
                hash[a] += 1
                temp_count += hash[a] == count

                if j >= size:
                    temp_count -= hash[s[j - size]] == count
                    hash[s[j - size]] -= 1
                
                if temp_count == i:
                    res += 1

            hash.clear()
        return res