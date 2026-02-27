class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        one = ''
        zero = ''
        for n in s:
            if n=='1':
                one+=n
            else:
                zero+=n
        if len(one) > len(zero):
            return True
        else:
            return False