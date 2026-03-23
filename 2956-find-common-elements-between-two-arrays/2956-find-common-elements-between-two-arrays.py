class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
    
        count1 = 0
        for n in nums1:
            if n in set2:
                count1 += 1
    
        count2 = 0
        for n in nums2:
            if n in set1:
                count2 += 1
    
        return [count1, count2]