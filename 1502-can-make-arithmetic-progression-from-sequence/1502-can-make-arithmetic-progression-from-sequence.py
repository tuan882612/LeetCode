class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        if n == 2:
            return True
        arr.sort()
        diff = arr[0] - arr[1]
        for i in range(1, n):
            if diff != arr[i-1] - arr[i]:
                return False
        return True

