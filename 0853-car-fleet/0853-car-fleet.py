class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        good = []
        
        for pos, spd in sorted(zip(position, speed)):
            dist = target-pos
            good.append(dist/spd)

        res = 0
        curr = 0
    
        for i in good[::-1]:
            if i > curr:
                res += 1
                curr = i
                
        return res