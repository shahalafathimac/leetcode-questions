class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        for n in hours:
            if n >= target:
                count += 1
        return count