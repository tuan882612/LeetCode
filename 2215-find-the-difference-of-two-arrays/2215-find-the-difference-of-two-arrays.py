class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        temp = set()
        for i in nums1:
            if i not in nums2:
                temp.add(i)
        res.append(list(temp))
        temp = set()
        for i in nums2:
            if i not in nums1:
                temp.add(i)
        res.append(list(temp))
        return res