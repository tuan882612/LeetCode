class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}
        
        for i in list(set(nums1)) + list(set(nums2)):
            if i not in hash:
                hash[i] = 0
            hash[i] += 1
            
        return [k for k, v in hash.items() if v == 2]