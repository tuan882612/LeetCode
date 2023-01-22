class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        arr = [row[k] for row in score]
        sorted_arr = sorted(arr, reverse=True)
        hash = {row[k]:row for row in score}
        return [hash[i] for i in sorted_arr]
        
        