class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 1
        s = 0
        b = str(n)
        for i in b:
            p *= int(i)
            s += int(i)
        return p-s

