class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
#         track = logs[0][1]
#         res = logs[0][0]
        
#         for i in range(1,len(logs)):
#             t = abs(logs[i-1][1]-logs[i][1])
#             print(t)
#             if track < t:
#                 track = t
#                 res = logs[i][0]

        track = 0
        cur = 0
        res = logs[0][0]
        
        for i, t in logs:
            num = abs(cur-t)

            if num > track:
                track = num
                res = i
            elif num == track:
                track = num
                res = min(res,i)
                
            cur = t
        return res