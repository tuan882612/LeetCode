class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cur = sum(arr[:k-1])
        ref = k*threshold
        res = 0
        
        for i in range(k-1, len(arr)):
            cur += arr[i]
            
            if cur >= ref:
                res += 1
                
            cur -= arr[i-k+1]

        return res