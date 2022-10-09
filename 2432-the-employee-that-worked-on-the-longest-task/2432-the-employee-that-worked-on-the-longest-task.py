class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        track = 0
        prev = 0
        res = logs[0][0]
        
        for i, t in logs:
            num = abs(prev-t)

            if num > track:
                track = num
                res = i
            elif num == track:
                track = num
                res = min(res,i)
                
            prev = t
        return res