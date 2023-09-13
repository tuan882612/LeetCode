class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] < 10:
            return digits
        
        dq = deque(digits)

        for i in range(len(dq)-2, -1, -1):
            if dq[i+1] > 9:
                dq[i] += 1
                dq[i+1] = 0

        if dq[0] > 9:
            dq[0] = 0
            dq.appendleft(1)

        return dq