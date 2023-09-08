class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        elif n == 2:
            return [[1], [1,1]]

        res = [[1], [1,1]]

        for i in range(2, n):
            temp = [1]

            for j in range(1, len(res[i-1])):
                temp.append(res[i-1][j-1]+res[i-1][j])

            res.append(temp + [1])

        return res