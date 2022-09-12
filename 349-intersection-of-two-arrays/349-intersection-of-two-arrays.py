class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [k for k, v in Counter(list(set(nums1)) + list(set(nums2))).items() if v == 2]