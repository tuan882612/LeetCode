class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        hash = {}
        left = 0
        res = 0

        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1

        for index, val in enumerate(s):
            if hash[val] < k:
                res = max(res, self.longestSubstring(s[left:index],k))
                left = index + 1

        if left == 0:
            return len(s)
        
        return max(res, self.longestSubstring(s[left:], k))