class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        arr = list(sorted(boxTypes, key = lambda x:x[1], reverse=1))
        res = 0
        
        for count, type in arr:
            count = min(count, truckSize)

            res += count*type
            truckSize -= count

            if truckSize == 0:
                return res

        return res