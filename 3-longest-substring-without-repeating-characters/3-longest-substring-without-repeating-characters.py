class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        res = left = 0
        for start in range(len(s)+1):
            temp = s[left:start]
            for j in temp:
                if j not in hash:
                    hash[j] = 1
                else:
                    hash[j] += 1
                if hash[j] > 1:
                    left += 1
                    break
            res = max(res, len(hash))
            hash.clear()
        return res