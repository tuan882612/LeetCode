class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = []
        
        for i in zip(*matrix):
            arr.append(list(i))
            
        return arr