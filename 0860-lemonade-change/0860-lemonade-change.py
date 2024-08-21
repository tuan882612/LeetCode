class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        res = 0
        n5 = n10 = 0
        
        for b in bills:
            if b == 10:
                if n5 > 0:
                    n10 += 1
                    n5 -= 1
                    res += b - 5
                else:
                    return False
            elif b == 20:
                if n10 > 0 and n5 > 0:
                    n10 -= 1
                    n5 -= 1
                    res += b - 15
                elif n5 > 2:
                    n5 -= 3
                    res += b - 15
                else:
                    return False
            else:
                n5 += 1
                res += 5

        return True