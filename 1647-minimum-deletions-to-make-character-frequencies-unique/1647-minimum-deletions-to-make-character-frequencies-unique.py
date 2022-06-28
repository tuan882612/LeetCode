class Solution:
    def minDeletions(self, s: str) -> int:
        hash = {}
        res = 0

        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1

        track = []

        for key, val in reversed(hash.items()):

            if val in track:

                while hash[key] in track and hash[key] != 0:
                    hash[key] -= 1
                    res += 1

            track.append(hash[key])

        return res