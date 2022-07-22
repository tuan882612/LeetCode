import collections

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        hash = collections.defaultdict(list)
        res = 0

        for i in words:
            hash[i[0]].append(i)

        for i in s:
            temp = hash[i]
            hash[i] = []

            for word in temp:
                if len(word) == 1:
                    res += 1
                else:
                    hash[word[1]].append(word[1:])

        return res