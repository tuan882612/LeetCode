from collections import defaultdict

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        ht = defaultdict(int)
        cur, res = 0, ""

        for msg, usr in zip(messages, senders):
            ht[usr] += msg.count(' ')+1

            if ht[usr] > cur or ht[usr] == cur and usr > res:
                cur = ht[usr]
                res = usr
                
        return res