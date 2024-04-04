class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n, diff = len(arr), abs(arr[0]-arr[1])
        if n == 2:
            return diff
            
        for i in range(2, n):
            if abs(arr[i-1]-arr[i]) != diff:
                return False

        return True
