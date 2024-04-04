class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = abs(arr[0]-arr[1])
        for i in range(2, len(arr)):
            if abs(arr[i-1]-arr[i]) != diff:
                return False

        return True
