import string

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        letter_map = {v:str(i + 1) for i, v in enumerate(string.ascii_lowercase)}
        new_s = "".join(letter_map.get(letter) for letter in s)
        for _ in range(k):
            new_s = str(sum(map(int, new_s)))
        return int(new_s)