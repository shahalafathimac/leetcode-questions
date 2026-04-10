class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num = []
        for n in nums1:
            if n in nums2 and n not in num:
                num.append(n)
        return num
