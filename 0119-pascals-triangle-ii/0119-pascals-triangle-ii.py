class Solution:
    def getRow(self, n: int) -> List[int]:
        if n == 0:
            return [1]
        if n <= 1:
            return [1, 1]

        res = [[1], [1,1]]

        for i in range(2, n+1):
            temp = [1]

            for j in range(1,len(res[i-1])):
                temp.append(res[i-1][j-1]+res[i-1][j])

            temp.append(1)
            res.append(temp)

        return res[n]