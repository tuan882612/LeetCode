class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        check=0
        for i in range(len(t)):
            if check < len(s) and s[check]==t[i]:
                    check+=1

        return check == len(s) 