class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:            
        arr = sorted([score[i][k] for i in range(len(score))], reverse=True)
        hash = {score[i][k]:score[i] for i in range(len(score))}
        return [hash[i] for i in arr]
        
        