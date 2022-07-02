class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        arr = list(sorted(boxTypes, key = lambda x:x[1], reverse=1))
        res = 0
        
        for i in arr:
            count = i[0]
            type = i[1]

            for j in range(1,count+1):
                if truckSize-1 == 0:
                    return res + type

                res += type
                truckSize -= 1

        return res