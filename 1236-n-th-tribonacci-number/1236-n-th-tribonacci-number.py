class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n <= 3:
            return n-1

        tab =  [0, 1, 1]

        for i in range(3, n):
            tab[i%3] = tab[0] + tab[1] + tab[2]

        return tab[0] + tab[1] + tab[2]