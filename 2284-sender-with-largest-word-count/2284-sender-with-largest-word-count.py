class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        ht = {}
        
        for msg, usr in zip(messages, senders):
            n = msg.count(' ')+1
            if usr not in ht:
                ht[usr] = n
            else:
                ht[usr] += n
                
        cur, res = 0, ""
        
        for k, v in ht.items():
            if v > cur:
                cur = v
                res = k
            elif v == cur and k > res:
                cur = v
                res = k
                
        return res