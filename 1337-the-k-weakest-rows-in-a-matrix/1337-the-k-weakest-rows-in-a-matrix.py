class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        minHeap=[]
        ans=[]
        heapq.heapify(minHeap)
        for row in range(len(mat)):
            soldiers=mat[row].count(1)
            heapq.heappush(minHeap,(soldiers,row))
        while k!=0:
            val,row=heapq.heappop(minHeap)
            ans.append(row)
            k-=1
        return ans