class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        arr = [1]*n 

        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                arr[i] = arr[i-1]+1

        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i] and arr[i+1] >= arr[i]:
                arr[i] = arr[i+1] + 1

        return sum(arr)