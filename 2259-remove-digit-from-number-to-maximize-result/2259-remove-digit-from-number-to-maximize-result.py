from locale import atoi

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        seen = set()
        res = 0

        for _ in range(number.count(digit)):

            for j in range(len(number)):

                if number[j] == digit and j not in seen:
                    seen.add(j)
                    res = max(atoi("".join(number[:j] + number[j+1:])), res)
                    break

        return str(res)
            
        
            