class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        pref = ""
        res = []

        for i in searchWord:
            pref += i
            temp = []

            for j in products:
                if len(temp)<3:
                    if j.startswith(pref):
                        temp.append(j)
                else:
                    break

            res.append(temp)

        return res